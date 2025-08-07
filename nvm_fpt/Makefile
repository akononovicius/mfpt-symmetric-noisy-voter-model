CC = gcc

SRC_DIR = src

LINKER_FLAGS = -lgsl -lgslcblas
OBJ_C_FLAGS = -c -fpic
OBJ_SO_FLAGS = -shared -o

all: libfpt.so

#
# SHARED OBJECTS
#
libfpt.so: fpt.o
	${CC} ${OBJ_SO_FLAGS} libfpt.so fpt.o ${LINKER_FLAGS}

#
# COMPONENT OBJECTS
#
fpt.o: ${SRC_DIR}/fpt.c ${SRC_DIR}/fpt.h
	${CC} ${OBJ_C_FLAGS} ${SRC_DIR}/fpt.c ${LINKER_FLAGS}

#
# GENERAL CMDS
#
clean:
	rm *.o

# vim: set noexpandtab tabstop=4 shiftwidth=4 softtabstop=-1:
