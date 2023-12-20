/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   get_next_line.h                                    :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: jusilanc <jusilanc@s19.be>                 +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2023/04/05 11:11:06 by jusilanc          #+#    #+#             */
/*   Updated: 2023/04/09 01:51:37 by jusilanc         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef GET_NEXT_LINE_H
# define GET_NEXT_LINE_H

# ifndef BUFFER_SIZE
#  define BUFFER_SIZE 8
# endif

# ifndef OPEN_MAX
#  define OPEN_MAX 1000
# endif

# include <stdlib.h>
# include <unistd.h>
# include <limits.h>

char	*get_next_line(int fd);
char	*ft_strndup(char *str, int n);
char	*ft_strchr(char *str, char c);
char	*ft_strstock(char *s1, char *s2, int param);
void	*ft_memmove(void *dst, const void *src, size_t len);
size_t	ft_strlen(char *str);

#endif
