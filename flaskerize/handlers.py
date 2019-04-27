def handle_bundle(args):
    target = args.bundle[0]
    if not target.endswith('/'):
        print("WARNING: Provided path '{}' does not end with "
              "'/', adding for you.".format(target))
        target += '/'


def handle_generate(args):
    from flaskerize import generate
    import os
    if len(args.generate) != 2:
        exit("ERROR: Invalid syntax found for generate. "
             "Correct usage is `flaskerize --generate type [args]`")

    what, called = args.generate

    if os.path.isfile(called) and not args.force:
        exit("ERROR: Target file '{}' already exists. "
             "Add --force to override".format(called))
    generate.a[what](called)