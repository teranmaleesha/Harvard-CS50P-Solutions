months = ["January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October", "November",
    "December"
]
while True:
    date = input("Date: ").strip("/")
    if "/" in date:
        try:
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)
            if 1 <= m <= 12 and 1<= d <= 31:
                print(f"{y:04d}-{m:02d}-{y:02d}")
                break
        except ValueError:
            pass
    elif "," in date:
        try:
            month_day, y = date.split(",")
            y = int(y.strip())
            month, d = month_day.split()
            month = month.title()
            d = int(d)
            if month in months and 1 <= d <= 31:
                m = months.index(month) + 1
                print(f"{y:04d}-{m:02d}-{d:02d}")
                break
        except ValueError:
            pass

