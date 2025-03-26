## 🔔 Latest Release Highlights

> 📅 **Released on: March 22, 2025**  
> 📢 **Common Lib v1.2.2** — Core logic updates packaged as `.whl`  
> 🧩 **Ingestion Framework v3.5.0** — Pipeline enhancements aligned with latest Common Lib

---

### 📦 Component Release Summary

| 🔧 Component          | 🔢 Version | 📅 Release Date | 🔄 Change Summary |
|----------------------|------------|------------------|--------------------|
| **Common Lib**       | `1.2.2`    | March 22, 2025   | Major logic revamp: schema evolution, SCD2, validations (packaged as `.whl`) |
| Ingestion Framework  | `v3.5.0`   | March 22, 2025   | Updated to invoke Common Lib v1.2.2, config template improvements |
| PyCobol              | `1.2.3`    | March 20, 2025   | COBOL field mapping improvements |
| XML Parser           | `1.3.4`    | March 18, 2025   | Streaming optimization for large XML files |

📄 [View Common Lib Release Notes](https://dev.azure.com/yourorg/yourproject/_git/demo?path=/common_lib/releases/v1.2.2.md)  
📄 [View Ingestion Framework Release Notes](https://dev.azure.com/yourorg/yourproject/_git/demo?path=/config/releases/v3.5.0.md)


## 🔗 Quick Access

- 📘 [Project Overview](./_portal/01_OVERVIEW.md)
- 📦 [Release Notes](./_portal/02_RELEASE_NOTES.md)
- 🔧 [Runbook](./_portal/03_RUNBOOK.md)
- 📄 [Common Lib Guide](./_portal/04_COMMON_LIB_GUIDE.md)
---

### 🧩 How Components Work Together

The **Common Lib** acts as the core processing engine, packaged as a `.whl` file.  
Ingestion pipelines are modular and lightweight — they orchestrate logic by invoking functions from the Common Lib.

> 💡 **Best Practice**: Always ensure the Ingestion Framework version aligns with the supported version of the Common Lib and other depedant Lib.  
Check the [compatibility matrix](https://dev.azure.com/yourorg/yourproject/_wiki/wikis/demo-wiki/Compatibility-Matrix) for more info.


