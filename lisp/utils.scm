(define (even? num)
  (= (remainder num 2) 0))

(define (square a)
  (* a a))

(define (gcd m n)
  (if (= n 0)
      m
      (gcd n (remainder m n))))
