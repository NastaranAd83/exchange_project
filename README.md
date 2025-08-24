 📌 پروژه صرافی (Exchange Project)

این پروژه یک سیستم ساده مدیریت صرافی است که با Django پیاده‌سازی شده و شامل مدیریت ارزها، قیمت ارزها، کارمندان و بدهی‌ها می‌باشد.  
تمرکز اصلی این پروژه روی "مدل‌سازی دیتابیس و روابط بین موجودیت‌ها" است.

---

📂 مدل‌ها و ارتباطات

🔹 BaseModel
- یک مدل انتزاعی (abstract) است.
- شامل فیلدهای عمومی مانند `created_at`، `updated_at` و `description`.
- همه‌ی مدل‌ها از این کلاس ارث‌بری می‌کنند.

---

🔹 CurrencyType
- نشان‌دهنده نوع ارز (مثل دلار، یورو، پوند).
- فیلدها:
  - `code` (مثل USD, EUR, GBP) – یکتا
  - `name` (نام فارسی یا انگلیسی ارز) – یکتا
- ارتباط‌ها:
  - **Many-to-Many** با `Exchange` از طریق مدل واسط `ExchangeCurrency`.
  - **One-to-Many** با `CurrencyPrice` (هر ارز می‌تواند قیمت‌های متعددی داشته باشد).

---

🔹 CurrencyPrice
- ذخیره تاریخچه‌ی قیمت ارزها.
- فیلدها:
  - `currency_code` → `ForeignKey` به `CurrencyType`
  - `price`, `date`, `time`
- هر بار که قیمت تغییر کند، یک رکورد جدید ذخیره می‌شود.

---
🔹 ExchangeAddress
- اطلاعات آدرس یک صرافی.
- ارتباط‌ها:
  - **One-to-One** با `Exchange`.

---
🔹 Exchange
- نشان‌دهنده یک صرافی.
- فیلد کلیدی: `exchange_zip_code`
- ارتباط‌ها:
  - **One-to-One** با `ExchangeAddress`.
  - **Many-to-Many** با `Staff` از طریق `ExchangeStaff`.
  - **Many-to-Many** با `CurrencyType` از طریق `ExchangeCurrency`.
  - **One-to-Many** با `ExchangePhone`.
  - **One-to-Many** با `Debt`.

---
🔹 ExchangePhone
- شماره تلفن‌های یک صرافی.
- ارتباط‌ها:
  - `ForeignKey` به `Exchange`.
- محدودیت: هر صرافی نمی‌تواند یک شماره تلفن را بیش از یک بار داشته باشد (`unique_together`).

---

🔹 ExchangeStaff
- مدل واسط برای ارتباط **Many-to-Many** بین `Exchange` و `Staff`.
- هر رکورد نشان‌دهنده‌ی حضور یک کارمند در یک صرافی است.
- محدودیت: ترکیب (exchange, staff) باید یکتا باشد.

---

🔹 ExchangeCurrency
- مدل واسط برای ارتباط **Many-to-Many** بین `Exchange` و `CurrencyType`.
- هر رکورد نشان‌دهنده پشتیبانی یک صرافی از یک ارز خاص است.
- محدودیت: ترکیب (exchange, currency) باید یکتا باشد.

---

🔹 Staff
- اطلاعات کارمندان صرافی.
- فیلد کلیدی: `national_code`
- ارتباط‌ها:
  - **Many-to-Many** با `Exchange` از طریق `ExchangeStaff`.
  - **One-to-Many** با `StaffPhone`.

---

🔹 StaffPhone
- شماره تلفن‌های کارمندان.
- ارتباط‌ها:
  - `ForeignKey` به `Staff`.
- محدودیت: هر کارمند نمی‌تواند یک شماره تلفن را بیش از یک بار داشته باشد (`unique_together`).

---

🔹 Debt
- بدهی‌های مربوط به یک صرافی.
- فیلدها شامل: مبلغ بدهی، تاریخ، وضعیت و توضیحات.
- ارتباط‌ها:
  - `ForeignKey` به `Exchange`.

---

📌 خلاصه ارتباط‌ها
- **Exchange <--> Staff** → Many-to-Many (از طریق ExchangeStaff)
- **Exchange <--> CurrencyType** → Many-to-Many (از طریق ExchangeCurrency)
- **Exchange -- ExchangeAddress** → One-to-One
- **Exchange -> ExchangePhone** → One-to-Many
- **Exchange -> Debt** → One-to-Many
- **Staff -> StaffPhone** → One-to-Many
- **CurrencyType -> CurrencyPrice** → One-to-Many

---

✍️ GitHub: NastaranAd83
