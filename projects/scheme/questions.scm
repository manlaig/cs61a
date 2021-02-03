(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

; Some utility functions that you may find useful to implement.

(define (cons-all first rests)
  (map (lambda (a) (append `(,first) a)) rests)
)

(define (zip pairs)
    (define a '())
    (define b '())
    (define a (map (lambda (v) (append a `,(car v))) pairs))
    (define b (map (lambda (v) (append b `,(car (cdr v)))) pairs))
    `(,a ,b)
)

;; Problem 16
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 16
  (define (helper lst count)
    (if (null? lst) ()
      (cons (list count (car lst)) (helper (cdr lst) (+ 1 count)))
    )
  )
  (helper s 0)
)
  ; END PROBLEM 16

;; Problem 17
;; List all ways to make change for TOTAL with DENOMS
(define (list-change total denoms)
  ; BEGIN PROBLEM 17
  (if (null? denoms) ()
    (if (= 0 total) `(nil)
      (if (> (car denoms) total)
          (list-change total (cdr denoms))
          (append (cons-all (car denoms) (list-change (- total (car denoms)) denoms))
                  (list-change total (cdr denoms))       )))   )
  ; END PROBLEM 17
)

;; Problem 18
;; Returns a function that checks if an expression is the special form FORM
(define (check-special form)
  (lambda (expr) (equal? form (car expr))))

(define lambda? (check-special 'lambda))
(define define? (check-special 'define))
(define quoted? (check-special 'quote))
(define let?    (check-special 'let))

;; Converts all let special forms in EXPR into equivalent forms using lambda
(define (let-to-lambda expr)
  (cond ((atom? expr)
         ; BEGIN PROBLEM 18
         expr
         ; END PROBLEM 18
         )
        ((quoted? expr)
         expr
         ; END PROBLEM 18
         )
        ((or (lambda? expr)
             (define? expr))
         (let ((form   (car expr))
               (params (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (cons form (cons params (map let-to-lambda body)))
           ; END PROBLEM 18
           ))
        ((let? expr)
         (let ((values (cadr expr))
               (body   (cddr expr)))
           ; BEGIN PROBLEM 18
           (define arr (zip values))
           ;((lambda (a b) (+ a b)) 1 2)
           (append `((lambda ,(car arr) ,(car (map let-to-lambda body)))) (map let-to-lambda (cadr arr)))
           ; END PROBLEM 18
           
           ))
        (else
         ; BEGIN PROBLEM 18
         (cons (car expr) (map let-to-lambda (cdr expr)))
         ; END PROBLEM 18
         )))
