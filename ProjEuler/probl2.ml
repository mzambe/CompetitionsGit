open Printf
open Array

let main () =
    let n = int_of_string (get Sys.argv 1) in
    let preprev = ref 1 in
    let prev = ref 2 in
    let this = ref 0 in
    let res = ref 2 in
    while (!this < n) do
        this := !prev + !preprev;
        preprev := !prev;
        prev := !this;
        if ((!this mod 2) == 0) then
            res := !res + !this
        else
            ();
    done;
    printf "result : %d \n" !res;;

let _ = Printexc.print main ();;
