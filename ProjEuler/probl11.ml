open Printf
open Scanf

let matrix n m init =
  let result = Array.make n (Array.make m init) in
    for i = 1 to n - 1 do
      result.(i) <- Array.make m init
    done;
    result;;

let thrmatrix n m l init =
    let result = Array.make n (matrix m l init) in
    for i = 1 to (n - 1) do
        result.(i) <- matrix m l init;
    done;
    result;;

let fourmatrix n m l p init = 
    let result = Array.make n (thrmatrix m l p init) in
    for i = 1 to (n - 1) do
        result.(i) <- thrmatrix m l p init;
    done;
    result;;

let n = ref 0;;
let m = ref 0;;

let eqtupl a b = match a with
    (a1, a2) -> match b with 
    (b1, b2) -> if ((b1 == a1) && (b2 == a2)) then true else false;;

let rec member ls l = match ls with
        [] -> false
    |   g::gs -> if (eqtupl g l) then true else (member gs l);;

let rec maxprod data i j k ls =
    let res = ref 0 in
    if ((i >= 0) && (j >= 0) && (i < !n) && (j < !m)) then
        begin
        if (k > 0) then
        begin
        let r11 = ref 0 in
        let r12 = ref 0 in
        let r13 = ref 0 in
        let r21 = ref 0 in
        let r23 = ref 0 in
        let r31 = ref 0 in
        let r32 = ref 0 in
        let r33 = ref 0 in
        r11 := if not (member ls (i-1, j-1)) then
            (data.(i).(j))*(maxprod data (i-1) (j-1) (k-1) ((i, j)::ls)) else 0;
        r12 := if not (member ls (i-1, j)) then
            (data.(i).(j))*(maxprod data (i-1) (j) (k-1) ((i, j)::ls)) else 0;
        r13 := if not (member ls (i-1, j+1)) then
            (data.(i).(j))*(maxprod data (i-1) (j+1) (k-1) ((i, j)::ls)) else 0;
        r21 := if not (member ls (i, j-1)) then
            (data.(i).(j))*(maxprod data (i) (j-1) (k-1) ((i, j)::ls)) else 0;
        r23 := if not (member ls (i, j+1)) then
            (data.(i).(j))*(maxprod data (i) (j+1) (k-1) ((i, j)::ls)) else 0;
        r31 := if not (member ls (i+1, j-1)) then
            (data.(i).(j))*(maxprod data (i+1) (j-1) (k-1) ((i, j)::ls)) else 0;
        r32 := if not (member ls (i+1, j)) then
            (data.(i).(j))*(maxprod data (i+1) (j) (k-1) ((i, j)::ls)) else 0;
        r33 := if not (member ls (i+1, j+1)) then
            (data.(i).(j))*(maxprod data (i+1) (j+1) (k-1) ((i, j)::ls)) else 0;
        res := (List.fold_right max [!r11; !r12; !r13; !r21; !r23; !r31; !r32; !r33] 0);
        end
        else
            res := data.(i).(j);
        end
    else
        res := 1;
    !res;;

let main () =
    n := scanf "%d " (fun x -> x);
    m := scanf "%d " (fun x -> x);
    let l = scanf "%d\n" (fun x -> x) in
    let res = ref 0 in
    let data = Array.make_matrix !n !m 0 in
    let resm = fourmatrix !n !m l 3 0 in
    let resm3 = fourmatrix !n !m l 4 0 in
    let r1 = ref 0 in
    let r2 = ref 0 in
    let r3 = ref 0 in
    let r4 = ref 0 in
    for i = 0 to !n - 1 do
        for j = 0 to !m - 1 do
            if j < (!m - 1) then
                data.(i).(j) <- scanf "%d " (fun x -> x)
            else
                data.(i).(j) <- scanf "%d\n" (fun x -> x);
            resm.(i).(j).(0).(0) <- data.(i).(j);
            resm.(i).(j).(0).(1) <- data.(i).(j);
            resm.(i).(j).(0).(2) <- data.(i).(j);
            resm3.(i).(j).(0).(0) <- data.(i).(j);
            resm3.(i).(j).(0).(1) <- data.(i).(j);
            resm3.(i).(j).(0).(2) <- data.(i).(j);
            resm3.(i).(j).(0).(3) <- data.(i).(j);
        done;
    done;
    for k = 1 to l - 1 do
        (*printf "k : %d\n" k;*)
        for i = 0 to !n - 1 do
            for j = 0 to !m - 1 do
                (*calc of .(0) *)
                r1 := if ((j > 0) && (i < (!n - 1))) then ((resm.(i + 1).(j - 1).(k - 1).(1))*(data.(i).(j))) else 1;
                r2 := if (j > 0) then (resm.(i).(j - 1).(k - 1).(1)*data.(i).(j)) else 1;
                r3 := if (i > 0) then (resm.(i - 1).(j).(k - 1).(1)*data.(i).(j)) else 1;
                r4 := if ((j > 0) && (i > 0)) then ((resm.(i-1).(j-1).(k-1).(1))*(data.(i).(j))) else 1;
                resm.(i).(j).(k).(0) <- max (max !r2 (max !r3 !r4)) !r1;

                r1 :=  if ((i > 0) && (j < (!m - 1))) then ((resm.(i - 1).(j + 1).(k - 1).(2))*(data.(i).(j))) else 1;
                r2 := if (j > 0) then (resm.(i).(j - 1).(k - 1).(2)*data.(i).(j)) else 1;
                r3 := if (i > 0) then (resm.(i - 1).(j).(k - 1).(2)*data.(i).(j)) else 1;
                r4 := if ((j > 0) && (i > 0)) then ((resm.(i - 1).(j - 1).(k - 1).(2))*(data.(i).(j))) else 1;
                resm.(i).(j).(k).(0) <- max (max (max !r1 !r2) (max !r3 !r4)) resm.(i).(j).(k).(0);

                resm3.(i).(j).(k).(0) <- if ((i < (!n - 1)) && (j < (!m - 1))) then
                                            data.(i).(j)*resm3.(i+1).(j+1).(k-1).(0)
                                         else
                                            data.(i).(j);

                (*calc of .(1) *)
                r1 :=  if ((j > 0) && (i < (!n - 1))) then ((resm.(i + 1).(j - 1).(k - 1).(1))*(data.(i).(j))) else 1;
                r2 := if (j > 0) then (resm.(i).(j - 1).(k - 1).(1)*data.(i).(j)) else 1;
                r3 := if (i > 0) then (resm.(i - 1).(j).(k - 1).(1)*data.(i).(j)) else 1;
                r4 := if ((j > 0) && (i > 0)) then ((resm.(i-1).(j-1).(k-1).(1))*(data.(i).(j))) else 1;
                resm.(i).(j).(k).(1) <- max (max !r1 !r2) (max !r3 !r4);

                r1 := 1;
                r2 := if (j > 0) then (resm.(i).(j - 1).(k - 1).(2)*data.(i).(j)) else 1;
                r3 := if (i > 0) then (resm.(i - 1).(j).(k - 1).(2)*data.(i).(j)) else 1;
                r4 := if ((j > 0) && (i > 0)) then ((resm.(i - 1).(j - 1).(k - 1).(2))*(data.(i).(j))) else 1;
                resm.(i).(j).(k).(1) <- max (max (max !r1 !r2) (max !r3 !r4)) resm.(i).(j).(k).(1);

                resm3.(i).(j).(k).(1) <- if ((i < (!n - 1)) && (j > 0)) then
                                            data.(i).(j)*resm3.(i+1).(j-1).(k-1).(1)
                                         else
                                            data.(i).(j);

                (*calc of .(2) *)
                r1 := 1;
                r2 := if (j > 0) then (resm.(i).(j - 1).(k - 1).(1)*data.(i).(j)) else 1;
                r3 := if (i > 0) then (resm.(i - 1).(j).(k - 1).(1)*data.(i).(j)) else 1;
                r4 := if ((j > 0) && (i > 0)) then ((resm.(i-1).(j-1).(k-1).(1))*(data.(i).(j))) else 1;
                resm.(i).(j).(k).(2) <- max (max !r1 !r2) (max !r3 !r4);

                r1 :=  if ((i > 0) && (j < (!m - 1))) then ((resm.(i - 1).(j + 1).(k - 1).(2))*(data.(i).(j))) else 1;
                r2 := if (j > 0) then (resm.(i).(j - 1).(k - 1).(2)*data.(i).(j)) else 1;
                r3 := if (i > 0) then (resm.(i - 1).(j).(k - 1).(2)*data.(i).(j)) else 1;
                r4 := if ((j > 0) && (i > 0)) then ((resm.(i - 1).(j - 1).(k - 1).(2))*(data.(i).(j))) else 1;
                resm.(i).(j).(k).(2) <- max (max (max !r1 !r2) (max !r3 !r4)) resm.(i).(j).(k).(2);

                resm3.(i).(j).(k).(2) <- if ((i < (!n - 1))) then
                                            data.(i).(j)*resm3.(i+1).(j).(k-1).(0)
                                         else
                                            data.(i).(j);

                resm3.(i).(j).(k).(3) <- if ((j < (!m - 1))) then
                                            data.(i).(j)*resm3.(i).(j+1).(k-1).(0)
                                         else
                                            data.(i).(j);

                (*printf "0 : %d, 1 : %d, 2 : %d    | " resm.(i).(j).(k).(0)
                 * resm.(i).(j).(k).(1) resm.(i).(j).(k).(2);*)
                if (!res < resm.(i).(j).(k).(0)) then
                    res := resm.(i).(j).(k).(0);
            done;
            (*printf "\n";*)
        done;
    done;
    let resm2 = matrix !n !m 0 in
    let res2 = ref 0 in
    let res3 = ref 0 in
    let resi = ref 0 in
    let resj = ref 0 in
    let ori = ref 0 in
    for i = 0 to (!n - 1) do
        for j = 0 to (!m - 1) do
            resm2.(i).(j) <- maxprod data i j (l-1) [];
            if (!res3 < resm3.(i).(j).(l-1).(0)) then
                begin
                resi := i;
                resj := j;
                ori := 0;
                res3 := resm3.(i).(j).(l-1).(0);
                end;
            if (!res3 < resm3.(i).(j).(l-1).(1)) then
                begin
                res3 := resm3.(i).(j).(l-1).(1);
                resi := i;
                resj := j;
                ori := 1;
                end;
            if (!res3 < resm3.(i).(j).(l-1).(2)) then
                begin
                res3 := resm3.(i).(j).(l-1).(2);
                resi := i;
                resj := j;
                ori := 2;
                end;
            if (!res3 < resm3.(i).(j).(l-1).(3)) then
                begin
                resi := i;
                resj := j;
                ori := 3;
                res3 := resm3.(i).(j).(l-1).(3);
                end;
            if (!res2 < resm2.(i).(j)) then
            begin
                res2 := resm2.(i).(j);
            end;
        done;
    done;

    printf "my result : %d my 2 result : %d resi : %d resj : %d orientation : %d \n" !res3 !res2 !resi !resj !ori;;

let _ = Printexc.print main ();;
