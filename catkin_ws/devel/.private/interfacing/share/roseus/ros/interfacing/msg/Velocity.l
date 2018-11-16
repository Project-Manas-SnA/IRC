;; Auto-generated. Do not edit!


(when (boundp 'interfacing::Velocity)
  (if (not (find-package "INTERFACING"))
    (make-package "INTERFACING"))
  (shadow 'Velocity (find-package "INTERFACING")))
(unless (find-package "INTERFACING::VELOCITY")
  (make-package "INTERFACING::VELOCITY"))

(in-package "ROS")
;;//! \htmlinclude Velocity.msg.html


(defclass interfacing::Velocity
  :super ros::object
  :slots (_Check _leftwheel _rightwheel ))

(defmethod interfacing::Velocity
  (:init
   (&key
    ((:Check __Check) 0)
    ((:leftwheel __leftwheel) 0.0)
    ((:rightwheel __rightwheel) 0.0)
    )
   (send-super :init)
   (setq _Check (round __Check))
   (setq _leftwheel (float __leftwheel))
   (setq _rightwheel (float __rightwheel))
   self)
  (:Check
   (&optional __Check)
   (if __Check (setq _Check __Check)) _Check)
  (:leftwheel
   (&optional __leftwheel)
   (if __leftwheel (setq _leftwheel __leftwheel)) _leftwheel)
  (:rightwheel
   (&optional __rightwheel)
   (if __rightwheel (setq _rightwheel __rightwheel)) _rightwheel)
  (:serialization-length
   ()
   (+
    ;; int8 _Check
    1
    ;; float32 _leftwheel
    4
    ;; float32 _rightwheel
    4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int8 _Check
       (write-byte _Check s)
     ;; float32 _leftwheel
       (sys::poke _leftwheel (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;; float32 _rightwheel
       (sys::poke _rightwheel (send s :buffer) (send s :count) :float) (incf (stream-count s) 4)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int8 _Check
     (setq _Check (sys::peek buf ptr- :char)) (incf ptr- 1)
     (if (> _Check 127) (setq _Check (- _Check 256)))
   ;; float32 _leftwheel
     (setq _leftwheel (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;; float32 _rightwheel
     (setq _rightwheel (sys::peek buf ptr- :float)) (incf ptr- 4)
   ;;
   self)
  )

(setf (get interfacing::Velocity :md5sum-) "50ef263368455a7e4548bab29e60b833")
(setf (get interfacing::Velocity :datatype-) "interfacing/Velocity")
(setf (get interfacing::Velocity :definition-)
      "int8 Check
float32 leftwheel
float32 rightwheel

")



(provide :interfacing/Velocity "50ef263368455a7e4548bab29e60b833")


