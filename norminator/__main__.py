# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __main__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/03/31 00:28:51 by ariard            #+#    #+#              #
#    Updated: 2017/03/31 19:46:30 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import subprocess
import re 

from error.error import *

if __name__ == '__main__':
    proc = subprocess.run(["norminette"], stdout=subprocess.PIPE)
    lst_files = re.split('Norme', str(proc.stdout))
    for i in lst_files:
        lst_error = i.split('\\n')
        for j in lst_error[1:]:
            error = normError(j)
            error.lexer()
#            error.func()
#            print(j)
#           print()
#            error = syntaxError(j)
