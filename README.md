w3a_scan_console 是什么？
=========================

    W3A SCAN 是一个新开启的项目，基于Python作为底层语言做的Web扫描器。
预备实现的功能涵盖以下功能：

- Web Sprider (页面爬虫) -----------------------------------------[Ok][100%]
- Web Page (Form/AJAX) distinguish (页面(表单|ajax)识别) ---------[OK][100%]
- Nmap Scanning (Nmap扫描模块) -----------------------------------[Ok][100%]
- Web Directory probe (目录探测) ---------------------------------[Filed][50%]
- Web Cross-Site script probe (跨站脚本探测) ---------------------[Filed][0%]
- Web Sql inject probe (SQL注入探测) -----------------------------[Filed][0%]
- Web Fingerprint (指纹识别) -------------------------------------[Filed][0%]
- Web LFI/RFI file contains(远程/本地文件包含) -------------------[Filed][0%]
- Follow-up update..... (后续更新...)


Structure(结构)
=======================

- config/  --------------------[配置目录]
- --config.ini  --------------[数据库配置]
- log/ -----------------[错误日志]
- main.py--------------[主程序]
- module/ ---------------[程序检测模块]
- --db_module.py -------[数据库模块]
- --form-test_module.py ------[页面(表单|ajax)识别模块]
- --nmap_module.py -------------[Nmap扫描模块]
- --sprider_module.py ---------[页面爬虫模块]
- --directory-test_module.py -----[目录探测模块]


Help (帮助)
========================
   前期编写的都是以模块的形式出现，后期当框架建立起来以后，将会扫瞄的模块将会以
插件的形式出现。目前的想法主要是想将一些常见的功能实现出来，待后续需求确定以后再
对整个扫瞄的架构进行调整。


Readme (说明)
========================
  - 1) 该项目会长期维护，后续会有web界面.(W3a Scan)
  - 2) 该项目更新的方式主要是以git更新的方式为准
  - 3) 模块的进度意义：
      --10% 构思完成
      --20% 代码正在编写
      --30%-50% 代码正在更新,细节正在重写
      --60%-80% 代码正在测试,修复bug和测试模块是否可用
      --90% 校正bug,留下使用例子,确定插入sql结构
      --100% 基本功能实现完成

FindMe (找我)
=======================
  - Name: Smart
  - QQ:505575655
  - Email: tangyucong@163.com
