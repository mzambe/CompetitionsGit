open Printf
open Scanf

let matrix n m init =
  let result = Array.make n (Array.make m init) in
    for i = 1 to n - 1 do
      result.(i) <- Array.make m init
    done;
    result;;

let n = ref 0;;

let rec maximumsum i j table =
    let res = ref 0 in
    if (i < (!n - 1)) then
    begin
        res := table.(i).(j) + (max (maximumsum (i+1) j table) (maximumsum (i+1) (j+1) table));
    end
    else
        res := table.(i).(j);
    !res;;

let main () =
    n := scanf "%d\n" (fun x -> x);
    let res = ref 0 in
    let data = Array.make_matrix !n !n 0 in
    for i = 0 to !n - 1 do
        for j = 0 to i do
            if j < i then
                data.(i).(j) <- scanf "%d " (fun x -> x)
            else
                data.(i).(j) <- scanf "%d\n" (fun x -> x);
        done;
    done;
    res := maximumsum 0 0 data;
    printf "my result : %d \n" !res;;

let _ = Printexc.print main ();;
