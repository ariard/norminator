# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __main__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/03/31 00:28:51 by ariard            #+#    #+#              #
#    Updated: 2017/04/04 20:50:32 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import re 
import sys

from lexer.lexer import *
from parser.parser import *
from solver.solver import *

if __name__ == '__main__':

    args = ["norminette"];
    for argv in sys.argv[1:]:
        args.append(argv)
    proc = subprocess.run(args, stdout=subprocess.PIPE)

    # Split to a list of files and lex, parse and exec at the fly

    lst_files = re.split('Norme', str(proc.stdout))
    iterator_file = iter(args[1:])
    for i in lst_files:
        lst_error = i.split('\\n')

        # Lexer errors following convention : LINE - ERROR - (KEYWORD)

        lst_tokens = list()
        for j in lst_error[1:]:
            lst_tokens.append(lexer(j))  

        # Destroy identic errors then parse token following convention
        # - type
        # - solver
        # - keydata
        # - more

        parser_destroy_superflous(lst_tokens) 
        lst_solv = list()
        for tokens in lst_tokens:
            lst_solv.append(parser(tokens)) 

        # Open file and apply error solvers
        # If errors aren't soft, ignore

        
        fd = open(iterator_file.__next__(), 'r')
        iterator_solv = iter(lst_solv)      
        n = 0;
        for line in fd:
            error = iterator_solv.__next__()
            while n == error.line:
                if error.type == "soft":
                    error.solver(file)
                error = iterator_solv.__next()

#       write rapport with next iterator
