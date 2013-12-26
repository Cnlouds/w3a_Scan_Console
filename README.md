w3a_scan_console 是什么？
=========================

W3A SCAN 是一个新开启的项目，基于Python作为底层语言做的Web扫描器。预备实现的功能涵盖以下功能：

- Web Sprider (页面爬虫) -----------------------------------------[Ok]
- Web Page (Form/AJAX) distinguish (页面(表单|ajax)识别) ---------[OK]
- Nmap Scanning (Nmap扫描模块) -----------------------------------[Ok]
- Web Directory probe (目录探测) ---------------------------------[Filed]
- Web Cross-Site script probe (跨站脚本探测) ---------------------[Filed]
- Web Sql inject probe (SQL注入探测) -----------------------------[Filed]
- Web Fingerprint (指纹识别) -------------------------------------[Filed]
- Web LFI/RFI file contains(远程/本地文件包含) -------------------[Filed]
- Follow-up update..... (后续更新...) ----------------------------[Filed]


Structure(结构)
=======================

├── config  --------------------[配置目录]
│   └── config.ini  --------------[数据库配置]
├── LICENSE
├── log -----------------[错误日志]
├── main.py--------------[主程序]
├── module ---------------[程序检测模块]
│   ├── db_module.py -------[数据库模块]
│   ├── form-test_module.py ------[页面(表单|ajax)识别模块]
│   ├── nmap_module.py -------------[Nmap扫描模块]
│   └── sprider_module.py ---------[页面爬虫模块]
└── README.md


Help (帮助)
========================
Follow-up update
