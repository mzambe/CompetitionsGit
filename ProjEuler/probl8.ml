open Printf

let rec prod b = match b with
        [] -> 1
    |   a::ass -> a*(prod ass);;

let itoc b = (int_of_string (Char.escaped b));;

let main () =
    let n = (Array.get Sys.argv 1) in
    let fwid = ref [(itoc n.[0]); (itoc n.[1]); (itoc n.[2]); (itoc n.[3]); (itoc n.[4])] in
    let prev = ref 0 in
    (*printf "%c \n" n.[0];*)
    let res = ref 0 in
    for i = 5 to (String.length n) do
        prev := (prod !fwid);
        if (prev > res) then
            res := !prev;
        if (i <= ((String.length n) - 1)) then
            (fwid := List.tl !fwid;
            fwid := (!fwid) @ ([itoc n.[i]]))
        else
            ();
    done;
    printf "result : %d \n" !res;;

let _ = Printexc.print main ();;
