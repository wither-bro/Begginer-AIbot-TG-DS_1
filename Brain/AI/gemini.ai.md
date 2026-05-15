# 🧠 SERIES(CG) Studios: AI Brain Configuration

Этот каталог содержит настройки для интеграции с **Google Gemini API**. 
Является частью системы `Begginer-AIbot-TG/DS`.

---

## 🔐 Безопасность и Ключи

Файл с реальным ключом (`gemini.ai`) **строго запрещен** для публикации в открытом доступе. 
Он автоматически игнорируется системой Git благодаря правилу в `.gitignore`.

### 🛠 Как настроить доступ:

1. **Для локального запуска (A-Shell / PC):**
   - Создайте в этой папке файл `gemini.ai`.
   - Добавьте в него строку: `API_KEY=ваш_ключ`.
   - Получить ключ можно на [Google AI Studio](https://aistudio.google.com/).

2. **Для работы через GitHub Actions / Хостинг:**
   - Не создавайте файл с ключом в репозитории!
   - Зайдите в **Settings** -> **Secrets and variables** -> **Actions**.
   - Добавьте новый секрет с именем `GEMINI_KEY`.
   - Вставьте ваш API-ключ в поле значения.

---

## ⚙️ Технические характеристики
* **Core Engine:** Gemini 1.5 Pro / Flash
* **Module Path:** `Brain/AI/`
* **Status:** Protected by SERIES(CG) Security Protocol

---
> **Note from SERIES(CG) Studios:** "Code is Art, Education is Freedom." 🚀
