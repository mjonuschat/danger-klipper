# Stepper Driver Definitions

This page contains information to assist in defining the 'stepstick_type' config entry. If your driver is not on here, simply do not specify 'stepstick_type', and manually enter 'sense_resistor'.

> [!NOTE]
> Drivers with variable sense resistors (such as the FYSETC EXT2160) have not been defined and have been left out of the table intentionally. You must set sense resistor for them manually.


| Stepper Driver         | Sense Resistor | Max Current |
| ---------------------- | -------------- | ----------- |
| KRAKEN_2160_8A         | 0.022          | 8           |
| KRAKEN_2160_3A         | 0.022          | 3           |
| LEVIATHAN_5160         | 0.075          | 3           |
| LEVIATHAN_2209         | 0.11           | 2           |
| BTT_2208               | 0.11           | 2           |
| BTT_2209               | 0.11           | 2           |
| BTT_2240               | 0.11           | 2.1         |
| BTT_5160               | 0.075          | 3           |
| BTT_EZ_2130            | 0.11           | 2           |
| BTT_EZ_2208            | 0.11           | 2           |
| BTT_EZ_2209            | 0.11           | 2           |
| BTT_EZ_2225            | 0.11           | 2           |
| BTT_EZ_2226            | 0.11           | 2           |
| BTT_EZ_5160_PRO        | 0.075          | 2.5         |
| BTT_EZ_5160_RGB        | 0.05           | 4.7         |
| BTT_EZ_6609            | 0.11           | 2           |
| BTT_EXT_5160           | 0.022          | 10.6        |
| MELLOW_FLY_HV-TMC5160 Pro | 0.033       | 6           |
| COREVUS_2209           | 0.1            | 3           |
| COREVUS_2160_OLD       | 0.03           | 3           |
| COREVUS_2160_5A        | 0.03           | 5           |
| COREVUS_2160           | 0.05           | 3           |
| WATTEROTT_2100         | 0.11           | 1.2         |
| WATTEROTT_2130         | 0.11           | 1.2         |
| WATTEROTT_2208         | 0.11           | 1.2         |
| WATTEROTT_2209         | 0.11           | 1.7         |
| WATTEROTT_5160         | 0.075          | 3           |
| WATTEROTT_5160_HV      | 0.075          | 3           |
| FYSETC_2100            | 0.11           | 1.2         |
| FYSETC_2130            | 0.11           | 1.2         |
| FYSETC_2208            | 0.11           | 1.2         |
| FYSETC_2209            | 0.11           | 1.7         |
| FYSETC_2225            | 0.11           | 1.4         |
| FYSETC_2226            | 0.11           | 2           |
| FYSETC_HV5160          | 0.075          | 3           |
| FYSETC_QHV5160         | 0.075          | 3           |
| FYSETC_5161            | 0.06           | 3.5         |
| MKS_GC6609             | 0.11           | 2           |
| MKS_2130               | 0.11           | 2           |
| MKS_2208               | 0.11           | 2           |
| MKS_2209               | 0.11           | 2           |
| MKS_2225               | 0.11           | 2           |
| MKS_2226               | 0.17           | 2.5         |
| MKS_2240               | 0.11           | 2.1         |
