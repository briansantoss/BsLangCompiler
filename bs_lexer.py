import bs_core


def should_process_line(line: str) -> bool:
    return not line.startswith(bs_core.COMMENT_TOKEN) and line


def lexer(filepath):
    tokens = []

    with open(filepath, "r", encoding="utf-8") as src_file:
        for line_no, line in enumerate(src_file, start=1):
                stripped_line = line.rstrip()
                if should_process_line(stripped_line):
                    instruction_delim = stripped_line.find(" ")
                    if instruction_delim == -1:
                        instruction_tok = stripped_line.casefold()
                        args_toks = []
                    else:
                        instruction_tok = stripped_line[:instruction_delim].strip().casefold()
                        args_toks = [token.strip() for token in stripped_line[instruction_delim:].split(bs_core.ARG_SEPARATOR)]
                    
                    if instruction_tok not in bs_core.instruction_map:
                        print(f"Error at line {line_no}: Invalid commmand '{instruction_tok}'")  
                        exit(1)
                    
                    if len(args_toks) == 0:
                        print(f"Error at line {line_no}: No arguments provided")
                        exit(1)

                    tokens.append((instruction_tok, args_toks))
    return tokens