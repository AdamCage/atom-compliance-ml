# Контроль и управление изменениями в тендерных закупках
## Описание проекта

# Структура проекта

```bash
atom-compliance-ml
├─ .github                       # CI/CD
│  └─ workflows
│     ├─ check.yml
│     └─ release.yml
├─ .gitignore
├─ config                        # Ядро с конфигом
│  └─ config.yaml
├─ data                          # Данные для обучения и тестирования
│  ├─ ds
│  │  ├─ ds.unl
│  ├─ raw_data                   # Сырые данные для обучения
│  │  ├─ HMI                     # UC-визы
│  │  ├─ SSTS                    # SSTS-визы
│  │  └─ train_data_markup.xlsx  # Размеченные наблюдеия для обучения
│  └─ test_data                  # Тестовые данные
│     ├─ HMI                     # UC-визы
│     └─ SSTS                    # SSTS-визы
├─ doc
├─ inference                     # Директория для инфереса (FULL LAUNCH)
│  ├─ logs                       # Логи инференса
│  └─ submissions                # Директория результатов инференса (submissions)
├─ LICENSE
├─ models                        # Артифакты модели, графики, метрики и т.д.
└─ src                           # Ноутбуки для обучения и экспериментов, модули
   ├─ modules
   └─ notebooks

```

# Инструкция по работе с проектом
## Создание виртуальной среды

## Режим обучения

## Режим инференса (FULL LAUNCH)

# Контакты
Если у вас есть вопросы или предложения по проекту, пожалуйста, свяжитесь с нами:
- Богдан, TL
   - @AdamCage
- Светлана, DS
   - @Wolta_1
- Егор, DevOps
   - @egor_lyadsky
- Александр, DS
   - @BeesKnights
