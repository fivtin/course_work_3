from datetime import datetime


def get_formatted_isodatetime(iso_format: str, format_str="%d.%m.%Y"):
    """convert date from iso format to specified format"""
    return datetime.fromisoformat(iso_format).strftime(format_str)
