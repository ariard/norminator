# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    error.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ariard <ariard@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2017/03/31 18:48:01 by ariard            #+#    #+#              #
#    Updated: 2017/03/31 20:11:42 by ariard           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re

class normError():
    def __init__(self, str):
        self.str = str
    
    def lexer(self):
        self.line = re.search(r'\d+', self.str)
        print(self.line)
