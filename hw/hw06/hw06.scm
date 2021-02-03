;;;;;;;;;;;;;;;
;; Questions ;;
;;;;;;;;;;;;;;;

; Scheme

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (cond ((> x 0) 1)
        ((< x 0) -1)
        (else 0) )
)

(define (square x) (* x x))

(define (pow b n)
  (if (eq? n 0)
    1
    (if (odd? n)
      (* b (pow b (- n 1)))
      (square (pow b (/ n 2)))
    )
  )
)

(define (unique s)
  (if (null? s)
    ()
    (cons (car s) (unique (filter (lambda (compare_num) (not (eq? compare_num (car s))))(cdr s)))
  )
))