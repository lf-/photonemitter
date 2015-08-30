import photonemitter
from . import config
from . import output


def main():
    config = photonemitter.config.Configuration()
    ps = photonemitter.ProviderSet()
    for prov in config.providers:
        ps.add(**prov)

    while True:
        line = input()
        results = ps.query(line)
        if results is None:
            print()
        else:
            photonemitter.output.send(results)


main()
