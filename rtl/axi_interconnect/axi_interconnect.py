def setup(py_params_dict):
    attributes_dict = {
        "original_name": "axi_interconnect",
        "name": "axi_interconnect",
        "version": "0.1",
        "generate_hw": False,
        "confs": [
            {
                "name": "ID_WIDTH",
                "type": "P",
                "val": "8",
                "min": "NA",
                "max": "NA",
                "descr": "ID bus width",
            },
            {
                "name": "DATA_WIDTH",
                "type": "P",
                "val": "32",
                "min": "NA",
                "max": "NA",
                "descr": "Data bus width",
            },
            {
                "name": "ADDR_WIDTH",
                "type": "P",
                "val": "32",
                "min": "NA",
                "max": "NA",
                "descr": "Address bus width",
            },
            {
                "name": "M_ADDR_WIDTH",
                "type": "P",
                "val": "{M_COUNT{{M_REGIONS{32'd24}}}}",
                "min": "NA",
                "max": "NA",
                "descr": "Master address bus width",
            },
            {
                "name": "S_COUNT",
                "type": "P",
                "val": "4",
                "min": "NA",
                "max": "NA",
                "descr": "Number of slave interfaces",
            },
            {
                "name": "M_COUNT",
                "type": "P",
                "val": "4",
                "min": "NA",
                "max": "NA",
                "descr": "Number of master interfaces",
            },
        ],
        "ports": [
            {
                "name": "clk_rst",
                "interface": {
                    "type": "clk_rst",
                    "subtype": "slave",
                },
                "descr": "Clock, clock enable and reset",
            },
            {
                "name": "s_axi",
                "interface": {
                    "type": "axi",
                    "subtype": "slave",
                    "port_prefix": "s_",
                    "mult": "S_COUNT",
                    "ID_W": "ID_WIDTH",
                    "ADDR_W": "ADDR_WIDTH",
                    "DATA_W": "DATA_WIDTH",
                    "LEN_W": "8",
                },
                "descr": "AXI slave interface",
            },
            {
                "name": "m_axi",
                "interface": {
                    "type": "axi",
                    "subtype": "master",
                    "port_prefix": "m_",
                    "mult": "M_COUNT",
                    "ID_W": "ID_WIDTH",
                    "ADDR_W": "ADDR_WIDTH",
                    "DATA_W": "DATA_WIDTH",
                    "LEN_W": "8",
                },
                "descr": "AXI master interface",
            },
        ],
        "blocks": [
            {
                "core_name": "arbiter",
                "instance_name": "arbiter_inst",
            },
        ],
    }

    return attributes_dict
