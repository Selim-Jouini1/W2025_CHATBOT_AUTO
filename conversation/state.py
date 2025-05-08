import logging

def update_state(state, new_data):
    for key, value in new_data.items():
        if value is not None and value != '':
            logging.debug(f"Updating state: {key} = {value}")
            state[key] = value
    return state
