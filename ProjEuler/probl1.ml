open Printf
open Array

let main () =
    let n = int_of_string (get Sys.argv 1) in
    let sum = ref 0 in
    for i = 1 to ((n - 1) / 3) do
        if ((3*i) mod 5) != 0 then
            sum := !sum + 3*i;
    done;
    for i = 1 to ((n - 1) / 5) do
        sum := !sum + 5*i;
    done;
    printf "Sum : %d \n" (!sum);;

let _ = Printexc.print main ();;
