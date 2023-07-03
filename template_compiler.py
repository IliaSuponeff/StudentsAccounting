import os.path
import shutil


def get_templates_files(template_dir: str | os.PathLike, *sub_dirs):
    templates_files = []
    see_dir = os.path.join(template_dir, *sub_dirs)
    for child in os.listdir(see_dir):
        child_abspath = os.path.join(see_dir, child)
        if os.path.isfile(child_abspath):
            if child.endswith('.ui'):
                templates_files.append((*sub_dirs, child,))
        elif os.path.isdir(child_abspath):
            templates_files += get_templates_files(template_dir, *(list(sub_dirs) + [child]))

    return templates_files


def create_init(save_path: str | os.PathLike):
    init_filepath = os.path.join(save_path, '__init__.py')
    with open(init_filepath, 'w', encoding='UTF-8') as file:
        file.write(
            f'"""\nPackage contains files which implementing visual of {os.path.basename(save_path).upper()} objects\n'
            f'@author: Ilia Suponev[https://github.com/ProgKalm?tab=repositories]\n'
            f'@version: 1.0.0\n"""\n'
        )
        file.write("\n\n# Uncomment the text below and create the correct imports\n")
        file.write("# from . import <imports>")


def get_python_filename(ui_filename: str):
    return 'ui_' + ui_filename.replace('.ui', '.py').lower().replace(' ', '_')


def get_convert_dict(template_dir: str | os.PathLike,
                     convert_dir: str | os.PathLike,
                     templates_files: tuple[tuple[str]]):
    convert_dict = dict()
    for filepath in templates_files:
        ui_filename: str = filepath[-1]
        sub_dirs: tuple[str] = filepath[:-1]
        save_path = os.path.abspath(convert_dir)
        for sub_dir in sub_dirs:
            save_path = os.path.join(save_path, sub_dir)
            if not os.path.exists(save_path):
                os.makedirs(save_path)
                create_init(save_path)

        # key - .ui template abspath, value - .py result file abspath
        py_filename = get_python_filename(ui_filename)
        convert_dict[os.path.join(template_dir, *filepath)] = os.path.join(
            convert_dir, *(list(sub_dirs) + [py_filename])
        )

    return convert_dict


def uicompile(template_file: str | os.PathLike, python_file_path: str | os.PathLike):
    os.system(
        f"pyside6-uic {template_file} -o {python_file_path}"
    )


def clear_dir(directory: os.PathLike | str):
    for child in os.listdir(directory):
        if '__init__.py' != child:
            path = os.path.join(directory, child)
            if os.path.isfile(path):
                os.remove(path)
            elif os.path.isdir(path):
                shutil.rmtree(path)


def main():
    root_dir = os.path.dirname(os.path.abspath(__file__))
    template_dir = os.path.join(root_dir, 'ui_templates')
    convert_dir = os.path.join(root_dir, 'src', 'views')
    clear_dir(convert_dir)
    templates_files = tuple(get_templates_files(template_dir))
    convert_dict = get_convert_dict(template_dir, convert_dir, templates_files)
    for template_file in convert_dict.keys():
        uicompile(template_file, convert_dict[template_file])


if __name__ == '__main__':
    main()
