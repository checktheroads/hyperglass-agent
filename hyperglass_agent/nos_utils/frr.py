from logzero import logger as log
from hyperglass_agent.constants import AFI_DISPLAY_MAP


async def parse_frr_output(raw, query_data, not_found):
    raw_split = raw.strip()
    if not raw_split:
        notfound_message = not_found.format(
            target=query_data.target, afi=AFI_DISPLAY_MAP[query_data.afi]
        )
        output = notfound_message
    else:
        output = raw_split
    log.debug(f"Parsed output:\n{output}")
    return output