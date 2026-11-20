"""Install the GN Frontier shader preset alongside a verified upstream copy."""

import argparse
import hashlib
from pathlib import Path
from urllib.error import URLError
from urllib.request import Request, urlopen


UPSTREAM_NAME = "ComplementaryUnbound_r5.9.3.zip"
UPSTREAM_URL = "https://edge.forgecdn.net/files/8884/656/" + UPSTREAM_NAME
UPSTREAM_SIZE = 553400
UPSTREAM_SHA256 = "98ac741dee294d2a3c82d153349148c3bb7fb688c30eb3b49c3b9ac37e968c5a"
PACK_NAME = "GN Frontier Shaders.zip"


def upstream_bytes(shaderpacks, base):
    existing = shaderpacks / UPSTREAM_NAME if base is None else base
    if base is not None or existing.exists():
        with existing.open("rb") as source:
            data = source.read(UPSTREAM_SIZE + 1)
    else:
        request = Request(UPSTREAM_URL, headers={"User-Agent": "GN-Frontier-Shaders/0.1.0"})
        with urlopen(request, timeout=45) as source:
            data = source.read(UPSTREAM_SIZE + 1)
    if len(data) != UPSTREAM_SIZE or hashlib.sha256(data).hexdigest() != UPSTREAM_SHA256:
        raise ValueError(f"Expected the official, unaltered {UPSTREAM_NAME} archive.")
    return data


def install(shaderpacks, base):
    archive = upstream_bytes(shaderpacks, base)
    profile = Path(__file__).with_name("gn-frontier.properties").read_bytes()
    files = ((shaderpacks / (PACK_NAME + ".txt"), profile), (shaderpacks / PACK_NAME, archive))

    pending = []
    for path, content in files:
        if path.exists():
            if path.read_bytes() != content:
                raise FileExistsError(f"Existing settings or pack differ and were preserved: {path}")
        else:
            pending.append((path, content))

    shaderpacks.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for path, content in pending:
            with path.open("xb") as destination:
                created.append(path)
                destination.write(content)
    except (OSError, KeyboardInterrupt):
        for path in reversed(created):
            path.unlink(missing_ok=True)
        raise


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("shaderpacks", type=Path, help="Shaderpacks folder for your Minecraft instance")
    parser.add_argument("--base", type=Path, help=f"Path to the official {UPSTREAM_NAME}")
    args = parser.parse_args()
    try:
        install(args.shaderpacks, args.base)
    except URLError as error:
        parser.exit(1, f"Download failed ({error.reason}). Download {UPSTREAM_NAME} and pass --base.\n")
    except (OSError, ValueError) as error:
        parser.exit(1, f"{error}\n")
    print(f"Installed {PACK_NAME} and its profile in {args.shaderpacks}.")


if __name__ == "__main__":
    main()
