def setup(py_params_dict):
    attributes_dict = {
        "original_name": "axi_interconnect",
        "name": "axi_interconnect",
        "version": "0.1",
        "generate_hw": False,
        "blocks": [
            {
                "core_name": "arbiter",
                "instance_name": "arbiter_inst",
            },
        ],
    }

    return attributes_dict
