def generate_registers_mux_sel(name, desc, addr, field_desc):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [generate_field_mux_sel(field_desc)])

def generate_registers_divcfg(name, desc, addr, mdmt):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [generate_field_divcfg(mdmt)])

def generate_registers_mux_sel_divcfg(name, desc, addr, field_desc, mdmt):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [
        generate_field_mux_sel(field_desc),
        generate_field_divcfg(mdmt)
    ])

def generate_registers_icg(name, desc, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [generate_field_icg()])

def generate_registers_icg_divcfg(name, desc, addr, mdmt):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [
        generate_field_icg(),
        generate_field_divcfg(mdmt)
    ])

def generate_registers_icg_mux_sel(name, desc, addr, field_desc):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [
        generate_field_icg(),
        generate_field_mux_sel(field_desc)
    ])

def generate_registers_dly_chain_sel(name, desc, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [generate_field_dly_chain_sel()])

def generate_registers_clk_polarity(name, desc, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, [generate_field_clk_polarity()])

def generate_registers_rst_sel(name, desc, idx, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, generate_field_rst_sel(idx))

def generate_registers_rst_stat(name, desc, addr):
    """Generate xml string for starfive_jh7110_stgcrg """ + name + """ register"""
    return generate_register(name, desc, addr, generate_field_rst_stat())

def generate_registers_aon_rst_sel(name, desc, addr):
    """Generate xml string for starfive_jh7110_syscrg """ + name + """ register"""
    return generate_register(name, desc, addr, generate_field_aon_rst_sel())

def generate_register(name, desc, addr, field_name_desc_range_access, size=32, reset_value=0):
    txt = """\
                <register>
                  <name>""" + name + """</name>
                  <description>""" + desc + """</description>
                  <addressOffset>""" + "0x{:x}".format(addr) + """</addressOffset>
                  <size>""" + str(size) + """</size>
                  <resetValue>""" + str(reset_value) + """</resetValue>
                  <fields>
"""

    for (n, d, r, a) in field_name_desc_range_access:
        txt += generate_field(n, d, r, a)

    return txt + """\
                  </fields>
                </register>
"""

def generate_field(name, desc, bit_range, access):
    if len(desc) == 0:
        desc = name

    return """\
                    <field>
                      <name>""" + name + """</name>
                      <description>""" + desc + """</description>
                      <bitRange>""" + bit_range + """</bitRange>
                      <access>""" + access + """</access>
                    </field>
"""

def generate_field_mux_sel(field_desc):
    return (
        "clk_mux_sel",
        "Clock multiplexing selector: " + field_desc,
        "[29:24]",
        "read-write",
    )

def generate_field_divcfg(mdmt):
    field_desc = "Clock divider coefficient: Max={}, Default={}, Min={}, Typical={}".format(mdmt[0], mdmt[1], mdmt[2], mdmt[3])

    return ("clk_divcfg", field_desc, "[23:0]", "read-write")

def generate_field_icg():
    return ("clk_icg", "1: Clock enable, 0: Clock disable", "[31:31]", "read-write")

def generate_field_dly_chain_sel():
    desc = "Selector delay chain stage number, totally 32 stages, -50 ps each stage. The register value indicates the delay chain stage number. For example, diy_chain_sel=1 means to delay 1 stage."

    return ("dly_chain_sel", desc, "[23:0]", "read-write")

def generate_field_clk_polarity():
    return ("clk_polarity", "1: Clock inverter, 0: Clock buffer", "[30:30]", "read-write") 

def generate_field_rst_sel(idx):
    names = [
        [
            "rstn_u0_jtag2apb_presetn", "rstn_u0_sys_syscon_presetn", "rstn_u0_sys_iomux_presetn", "rst_u0_u7mc_sft7110_rst_bus",
            "rst_u0_u7mc_sft7110_debug_reset", "rst_u0_u7mc_sft7110_rst_core0", "rst_u0_u7mc_sft7110_rst_core1", "rst_u0_u7mc_sft7110_rst_core2",
            "rst_u0_u7mc_sft7110_rst_core3", "rst_u0_u7mc_sft7110_rst_core4", "rst_u0_u7mc_sft7110_rst_core0_st", "rst_u0_u7mc_sft7110_rst_core1_st",
            "rst_u0_u7mc_sft7110_rst_core2_st", "rst_u0_u7mc_sft7110_rst_core3_st", "rst_u0_u7mc_sft7110_rst_core4_st", "rst_u0_u7mc_sft7110_trace_rst0",
            "rst_u0_u7mc_sft7110_trace_rst1", "rst_u0_u7mc_sft7110_trace_rst2", "rst_u0_u7mc_sft7110_trace_rst3", "rst_u0_u7mc_sft7110_trace_rst4",
            "rst_u0_u7mc_sft7110_trace_com_rst", "rst_u0_img_gpu_rstn_apb", "rst_u0_img_gpu_rstn_doma", "rst_u0_u7mc_sft7110_noc_bus_reset_apb_bus_n",
            "rst_u0_u7mc_sft7110_noc_bus_reset_axicfg0_axi_n", "rst_u0_u7mc_sft7110_noc_bus_reset_cpu_axi_n", "rst_u0_u7mc_sft7110_noc_bus_reset_disp_axi_n", "rst_u0_u7mc_sft7110_noc_bus_reset_gpu_axi_n",
            "rst_u0_u7mc_sft7110_noc_bus_reset_isp_axi_n", "rst_u0_u7mc_sft7110_noc_bus_reset_ddrc_n", "rst_u0_u7mc_sft7110_noc_bus_reset_stg_axi_n", "rst_u0_u7mc_sft7110_noc_bus_reset_vdec_axi_n",
        ],
        [
            "rstn_u0_sft7100_noc_bus_reset_venc_axi_n", "rstn_u0_axi_cfg1_dec_rstn_ahb", "rstn_u0_axi_cfg1_dec_rstn_main", "rstn_u0_axi_cfg0_dec_rstn_main",
            "rstn_u0_axi_cfg0_dec_rstn_main_div", "rstn_u0_axi_cfg0_dec_rstn_hifi4", "rstn_u0_ddr_sft7110_rstn_axi", "rstn_u0_ddr_sft7110_rstn_osc",
            "rstn_u0_ddr_sft7110_rstn_apb", "rstn_u0_dom_isp_top_rstn_dom_isp_top_ip_top_reset_n", "rstn_u0_dom_isp_top_rstn_dom_isp_top_rstn_isp_axi", "rstn_u0_dom_vout_top_rstn_dom_vout_top_rstn_vout_src",
            "rstn_u0_codaj12_rstn_axi", "rstn_u0_codaj12_rstn_core", "rstn_u0_codaj12_rstn_apb", "rstn_u0_wave511_rstn_axi",
            "rstn_u0_wave511_rstn_bpu", "rstn_u0_wave511_rstn_vce", "rstn_u0_wave511_rstn_apb", "rstn_u0_vdec_jpg_arb_jpgresetn",
            "rstn_u0_vdec_jpg_arb_mainresetn", "rstn_u0_aximem_128b_rstn_axi", "rstn_u0_wave420l_rstn_axi", "rstn_u0_wave420l_rstn_bpu",
            "rstn_u0_wave420l_rstn_vce", "rstn_u0_wave420l_rstn_apb", "rstn_u1_aximem_128b_rstn_axi", "rstn_u2_aximem_128b_rstn_axi",
            "rstn_u0_intmem_rom_sram_rstn_rom", "rstn_u0_cdns_qspi_rstn_ahb", "rstn_u0_cdns_qspi_rstn_apb", "rstn_u0_cdns_qspi_rstn_ref",
        ],
        [
            "rstn_u0_sdio_rstn_ahb", "rstn_u1_sdi_rstn_ahb", "rstn_u1_gmac5_axi64_aresetn_i", "rstn_u1_gmac5_axi64_hresetn_n",
            "rstn_u0_mailbox_presetn", "rstn_u0_ssp_spi_rstn_apb", "rstn_u1_ssp_spi_rstn_apb", "rstn_u2_ssp_spi_rstn_apb",
            "rstn_u3_ssp_spi_rstn_apb", "rstn_u4_ssp_spi_rstn_apb", "rstn_u5_ssp_spi_rstn_apb", "rstn_u6_ssp_spi_rstn_apb",
            "rstn_u0_i2c_rstn_apb", "rstn_u1_i2c_rstn_apb", "rstn_u2_i2c_rstn_apb", "rstn_u3_i2c_rstn_apb",
            "rstn_u4_i2c_rstn_apb", "rstn_u5_i2c_rstn_apb", "rstn_u6_i2c_rstn_apb", "rstn_u0_uart_rstn_apb",
            "rstn_u0_uart_rstn_core", "rstn_u1_uart_rstn_apb", "rstn_u1_uart_rstn_core", "rstn_u2_uart_rstn_apb",
            "rstn_u2_uart_rstn_core", "rstn_u3_uart_rstn_apb", "rstn_u3_uart_rstn_core", "rstn_u4_uart_rstn_apb",
            "rstn_u4_uart_rstn_core", "rstn_u5_uart_rstn_apb", "rstn_u6_uart_rstn_core", "rstn_u0_cdns_spdif_rstn_apb",
        ],
        [
            "rstn_u0_pwmdac_rstn_apb", "rstn_u0_pdm_4mic_rstn_dmic", "rstn_u0_pdm_4mic_rstn_apb", "rstn_u0_i2srx_3ch_rstn_apb",
            "rstn_u0_i2srx_3ch_rstn_bclk", "rstn_u0_i2stx_4ch_rstn_apb", "rstn_u0_i2stx_4ch_rstn_bclk", "rstn_u1_i2stx_4ch_rstn_apb",
            "rstn_u1_i2stx_4ch_rstn_bclk", "rstn_u0_tdm16slot_rstn_ahb", "rstn_u0_tdm16slot_rstn_tdm", "rstn_u0_tdm16slot_rstn_apb",
            "rstn_u0_pwm_8ch_rstn_apb", "rstn_u0_dskit_wdt_rstn_apb", "rstn_u0_dskit_wdt_rstn_wdt", "rstn_u0_can_ctrl_rstn_apb",
            "rstn_u0_can_ctrl_rstn_can", "rstn_u0_can_ctrl_rstn_timer", "rstn_u1_can_ctrl_rstn_apb", "rstn_u1_can_ctrl_rstn_can",
            "rstn_u1_can_ctrl_rstn_timer", "rstn_u0_si5_timer_rstn_apb", "rstn_u0_si5_timer_rstn_timer0", "rstn_u0_si5_timer_rstn_time10",
            "rstn_u0_si5_timer_rstn_timer2", "rstn_u0_si5_timer_rstn_timer3", "rstn_u0_int_ctrl_rstn_apb", "rstn_u0_temp_sensor_rstn_apb",
            "rstn_u0_temp_sensor_rstn_temp", "rstn_u0_jtag_certification_rst_n", "", "",
        ],
    ]

    desc = "1: Assert reset, 0: De-assert reset"

    return [(names[idx][i], desc, "[{}:{}]".format(i, i), "read-write") for i in range(32) if len(names[idx][i]) != 0]

def generate_field_rst_stat():
    names = [
        "rstn_u0_stg_syscon_presetn", "rst_u0_hifi4_rst_core", "rst_u0_hifi4_rst_axi", "rstn_u0_sec_top_hreesetn",
        "rst_u0_e2_sft7110_rst_core", "rstn_u0_dma1p_8ch_56hs_rstn_axi", "rstn_u0_dma1p_8ch_56hs_rstn_ahb", "rstn_u0_cdn_usb_rstn_axi",
        "rstn_u0_cdn_usb_rstn_usb_apb", "rstn_u0_cdn_usb_rstn_utmi_apb", "rstn_u0_cdn_usb_rstn_pwrup", "rstn_u0_plda_pcie_rstn_axi_mst0",
        "rstn_u0_plda_pcie_rstn_axi_slv0", "rstn_u0_plda_pcie_rstn_axi_slv", "rstn_u0_plda_pci_rstn_brg", "rstn_u0_plda_pcie_rstn_pcie",
        "rstn_u0_plda_pcie_rstn_apb", "rstn_u1_plda_pcie_rstn_axi_mst0", "rstn_u1_plda_pcie_rstn_axi_slv0", "rstn_u1_plda_pcie_rstn_axi_slv",
        "rstn_u1_plda_pcie_rstn_brg", "rstn_u1_plda_pcie_rstn_pcie", "rstn_u1_plda_pcie_rstn_apb",
    ]

    desc = "1: Assert reset, 0: De-assert reset"

    return [(names[i], desc, "[{}:{}]".format(i, i), "read-write") for i in range(23)]

def generate_field_aon_rst_sel():
    names = [
            "gmac5_axi64_rstn_axi", "gmac5_axi64_rstn_ahb", "aon_iomux_presetn", "pmu_rstn_apb",
            "pmu_rstn_wkup", "rtc_hms_rstn_apb", "rtc_hms_rstn_cal", "rtc_hms_rstn_osc32k",
    ]

    desc = "1: Assert reset, 0: De-assert reset"

    return [(names[i], desc, "[{}:{}]".format(i, i), "read-write") for i in range(8)]

def generate_fields_list_sram_config(name, base):
    return [
        ("{}_slp".format(name), "SRAM/ROM configuration. SLP: sleep enable, high active, default is low.", "[{}:{}]".format(base, base), "read-write"),
        ("{}_sd".format(name), "SRAM/ROM configuration. SD: shutdown enable, high active, default is low.", "[{}:{}]".format(base + 1, base + 1), "read-write"),
        ("{}_rtsel".format(name), "SRAM/ROM configuration. RTSEL: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 3, base + 2), "read-write"),
        ("{}_ptsel".format(name), "SRAM/ROM configuration. PTSEL: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 5, base + 4), "read-write"),
        ("{}_trb".format(name), "SRAM/ROM configuration. TRB: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 7, base + 6), "read-write"),
        ("{}_wtsel".format(name), "SRAM/ROM configuration. WTSEL: timing setting for debug purpose, default is 2'b01.", "[{}:{}]".format(base + 9, base + 8), "read-write"),
        ("{}_vs".format(name), "SRAM/ROM configuration. VS: timing setting for debug purpose, default is 1'b1.", "[{}:{}]".format(base + 10, base + 10), "read-write"),
        ("{}_vg".format(name), "SRAM/ROM configuration. VG: timing setting for debug purpose, default is 1'b1.", "[{}:{}]".format(base + 11, base + 11), "read-write")
    ]
