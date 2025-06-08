
main_str = input()
substr = input()


starts_with = lambda s, sub: s.startswith(sub)

print("True" if starts_with(main_str, substr) else "False")
