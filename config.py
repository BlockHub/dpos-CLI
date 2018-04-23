"""
A configuration dict we pickle and depickle to store values so the user does not need to
enter them every single time
"""
import constants as c

CONFIG = {
    # false if the configs have been set
    "virgin": True,
    "ark": {
        # names used by arky to initialize
        "arky": "ark",
        "coin_in_sat": c.ARK
    },
    "dark": {
        # names used by arky to initialize
        "arky": "dark",
        "coin_in_sat": c.ARK
    },
    "test_persona": {
        # names used by arky to initialize
        "arky": "tprs",
        "coin_in_sat": c.ARK
    },
    "kapu": {
        # names used by arky to initialize
        "arky": "kapu",
        "coin_in_sat": c.ARK
    }
}