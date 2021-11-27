import re

from repository import StreamRepository

REGEX = r"(?:https?:\/\/)?(?:[^@\n]+@)?(?:www\.)?([^:\/\n?]+)"


def set_links(data: dict, repository: StreamRepository):
    if data["links"]:
        for link in data["links"]:
            clean_domain = re.findall(REGEX, str(link))[0]
            repository.set(clean_domain)
        return {
            "status": "ok",
        }
    else:
        return {
            "status": "No links",
        }


def get_links_in_range(start: int, end: int, repository: StreamRepository):
    try:
        start, end = int(start), int(end)
        return {"domains": repository.get(start, end), "status": "ok"}
    except ValueError:
        mes = "Wrong time format. Example: api/visited_domains/?start=0&end=16"
        return {"status": mes}
