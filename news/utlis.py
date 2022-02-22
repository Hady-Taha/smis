def slugify(str):
    str = str.replace(" ", "-")
    str = str.replace(",", "-")
    str = str.replace("(", "-")
    str = str.replace(")", "")
    str = str.replace("؟", "")
    return str


def cover_directory_path(instance, filename):
    return f'covers/cover_{instance.title}/{filename}'
