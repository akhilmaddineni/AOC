# Compiler and flags
CC = clang
CFLAGS = -Wall -Wextra -O2 -Icommon $(shell pkg-config --cflags glib-2.0)
LDFLAGS = $(shell pkg-config --libs glib-2.0)

# Define all days and common files
DAYS = day01
COMMON_SRC = common/utils.c
COMMON_OBJS = $(COMMON_SRC:.c=.o)

# Targets for each day
all: $(DAYS)

# Use a different name for the output executable (e.g., `day01.out`)
$(DAYS): %: %/main.o $(COMMON_OBJS)
	$(CC) $(CFLAGS) $^ -o $@.out $(LDFLAGS)

# Rule for compiling common files
$(COMMON_OBJS): %.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Rule for compiling day-specific .c files
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# Clean up generated files
clean:
	rm -f $(DAYS:=.out)
	find . -name '*.o' -delete
