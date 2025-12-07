def transpose(text):
    input_rows = text.split('\n')
    output_rows = []

    max_row_length = max(len(row) for row in input_rows)

    for i in range(max_row_length):
        output_row = []
        for input_row in input_rows:
            if i < len(input_row): 
                output_row.append(input_row[i])
            else:
                output_row.append('\0')
        output_rows.append(''.join(output_row))

    cleaned_output_rows = [ 
        row.rstrip('\0').replace('\0', ' ')                   
        for row 
        in output_rows
    ]

    return '\n'.join(cleaned_output_rows)
