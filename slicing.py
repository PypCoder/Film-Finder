def string_slicing(original_string,substring,position):
    f_part=original_string[:position]
    s_part=original_string[position:]
    return f_part+" "+substring+s_part

def add_to_url(original_url, add_url):
    if "?" in original_url:
        separator = "&"
    else:
        separator = "?"
    genres_str = ",".join(add_url)
    updated_url = f"{original_url}{separator}with_genres={genres_str}"
    return updated_url

def genre_entry():
    ugenre = True
    u = ""
    genre = []
    while ugenre:
        genre += [input("Enter:")]
        u = input("Proceed(y/n):").lower()
        if u == "y":
            break
        elif u == "n":
            continue
        else:
            print("INVALID")
    return genre