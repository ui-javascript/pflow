# from rembg import remove

# @tofix 会代理报错
def remove_bg(input_path):
    print(input_path)
    output_path = input_path + ".out.jpg"
    with open(input_path, 'rb') as i:
        with open(output_path, 'wb') as o:
            input = i.read()
            output = remove(input)
            o.write(output)

    return output_path