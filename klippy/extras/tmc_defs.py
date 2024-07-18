STEPSTICK_SENSE_RESISTORS = {
    "KRAKEN_2160": 0.022,
    "LEVIATHAN_5160": 0.075,
    "LEVIATHAN_2209": 0.11,
    "BTT_2208": 0.11,
    "BTT_2209": 0.11,
    "BTT_5160": 0.075,
    "BTT_EZ_2130": 0.11,
    "BTT_EZ_2208": 0.11,
    "BTT_EZ_2209": 0.11,
    "BTT_EZ_2225": 0.11,
    "BTT_EZ_2226": 0.11,
    "BTT_EZ_5160_PRO": 0.075,
    "BTT_EZ_5160_RGB": 0.05,
    "BTT_EZ_6609": 0.11,
    "BTT_EXT_5160": 0.022,
    "MELLOW_EXT_5160": 0.033,
    "COREVUS_2160": 0.0,
    "WATTEROTT_2100": 0.11,
    "WATTEROTT_2130": 0.11,
    "WATTEROTT_2208": 0.11,
    "WATTEROTT_2209": 0.11,
    "WATTEROTT_5160": 0.075,
    "WATTEROTT_5160_HV": 0.075,
}


def step_driver_fetch(config):
    stepper_driver_type = config.get("stepstick_type")
    return STEPSTICK_SENSE_RESISTORS.get(stepper_driver_type)
