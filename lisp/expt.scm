(load "utils.scm")

(define (fast-expt a n)
  (cond ((= n 0) 1)
	((even? n) (* (fast-expt a (/ n 2))(fast-expt a (/ n 2))))
	(else (* a (fast-expt a (- n 1))))))

(define (fast-expt-let a n)
  (cond ((= n 0) 1)
	((even? n) (let ((t (fast-expt-let a (/ n 2))))
		     (square t)))
	(else (* a (fast-expt-let a (- n 1))))))

(define (fast-expt-status a n)
  (define (fast-expt-iter a n product)
    (cond ((= n 0) product)
	  ((even? n) (fast-expt-iter (square a) (/ n 2) product))
	  (else (fast-expt-iter a (- n 1) (* product a)))))
  (fast-expt-iter a n 1))

;; 1.17
(define (by a b)
  (define (double a)
    (+ a a))

  (define (halve a)
    (/ a 2))

  (cond ((= b 0) 0)
	((even? b) (by (double a) (halve b)))
	(else (+ a (by a (- b 1)))))
  )

(define (new-* a b)
  (define (double i)
    (+ i i))
  (define (halve i)
    (/ i 2))

  (define (new-*-iter a b sum)
    (cond ((= b 0) sum)
	  ((even? b) (new-*-iter (double a) (halve b) sum))
	  (else (new-*-iter a (- b 1) (+ sum a)))))
  (new-*-iter a b 0)
  )

