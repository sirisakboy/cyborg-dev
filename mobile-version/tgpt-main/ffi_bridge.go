package main

/*
#include <stdlib.h>
*/
import "C"

import (
	"fmt"
	"unsafe"
)

//export ExecuteCommand
func ExecuteCommand(command *C.char) *C.char {
	cmd := C.GoString(command)
	
	// TODO: Call your actual logic here
	response := fmt.Sprintf("Go Engine Received: %s", cmd)
	
	return C.CString(response)
}

//export FreeString
func FreeString(str *C.char) {
	C.free(unsafe.Pointer(str))
}

func main() {}
