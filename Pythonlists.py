routes = [
    "Nairobi-Kitui",
    "Mombasa-Malindi",
    "Nakuru-Eldoret",
    "Kisumu-Busia",
    "Nyeri-Meru",
    "Garissa-Wajir",
    "Isiolo-Marsabit",
    "Thika-Murang'a",
    "Nanyuki-Rumuruti",
    "Kitale-Webuye"
]
print("Initial routes:\n", routes)

routes.append("Machakos-Makueni")
routes.remove("Garissa-Wajir")
print("\nAfter adding and removing:\n", routes)

routes.sort()
print("\nSorted routes:\n", routes)
routes.reverse()
print("\nReversed routes:\n", routes)

count_N = sum(1 for r in routes if r.startswith("N"))
print("\nNumber of routes starting with 'N':", count_N)

long_routes = [r for r in routes if len(r) > 10]
print("\nRoutes longer than 10 characters:\n", long_routes)
