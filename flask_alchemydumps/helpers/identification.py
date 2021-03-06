# coding: utf-8

from flask import current_app


def get_bkp_dir():
    """
    :return: unipath object of the dir where backup files are saved
    """
    basedir = current_app.extensions['alchemydumps'].basedir
    bkp_dir = basedir.child('alchemydumps')
    if not bkp_dir.exists():
        bkp_dir.mkdir()
    return bkp_dir


def get_id(file_path):
    """
    :param file_path: unipath object of a file generated by AlchemyDumps
    :return: the backup numeric id
    """
    filename = file_path.stem
    parts = filename.split('-')
    try:
        return parts[2]
    except IndexError:
        return False


def get_list(date_id=False, files=False):
    """
    :param date_id: (optional) Backup file numeric id (if False, list
    everything)
    :param files: (optional) If you have already called get_list(), pass the
    file list to improve performance
    :return: The list of backup files from that id
    """
    if files:
        if date_id:
            output = [f for f in files if date_id in f.stem]
        else:
            output = files
    else:
        bkp_dir = get_bkp_dir()
        pattern = '*{}*'.format(date_id) if date_id else None
        output = [f.absolute() for f in bkp_dir.listdir(pattern)]
    return output


def get_ids(files=False):
    """
    :param files: (optional) If you have already called get_list(), pass the
    file list to improve performance
    :return: List all valid IDs from the backup folder
    """
    if not files:
        files = get_list()
    file_ids = list()
    for f in files:
        file_id = get_id(f)
        if file_id and not file_ids.count(file_id):
            file_ids.append(file_id)
    return file_ids
