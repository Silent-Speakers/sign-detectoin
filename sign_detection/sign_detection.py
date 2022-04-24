import cv2
import mediapipe as mp
import pyttsx3


class SignDetection:
    """
    A class that detects the hand landmarks.
        Translate the landmarks into a specific american sign language using the coordinates of each finger's landmark
        Translate the sign language to voice record
        Translate the sign language to an image
    """
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands()
        self.mp_draw = mp.solutions.drawing_utils
        self.cap = cv2.VideoCapture(0)
        self.output_list = []
        self.common = ''
        self.words = {'Like': False, 'Dislike': False, 'Stop': False, 'Forward': False, 'Backward': False,
                      'Right': False, 'Left': False, 'I love you': False, 'Yes': False, 'No': False, 'Victory': False,
                      'Nice': False, 'Yellow': False, 'Purple': False, 'Green': False}
        # For voice recognition
        self.letter = ""
        self.quit = 1


    def hand_detection(self):
        """
        A method that is used for detecting the landmarks for the fingers and translates it to sign language using the x and y coordinates
            Arguments: None
            Returns: Displays the hand landmarks, image, text and voice for each sign language

        """
        finger_tips = [8, 12, 16, 20]
        thumb_tip = 4
        index_tip = 8
        middle_tip = 12
        ring_tip = 16
        little_tip = 20

        while True:
            # Intialize the finger status with None
            index_tip_status_fh = None
            index_tip_status_fv = None
            index_tip_status_v = None
            index_tip_status_h = None
            middle_tip_status_fh = None
            middle_tip_status_fv = None
            middle_tip_status_v = None
            middle_tip_status_h = None
            little_tip_status_fh = None
            little_tip_status_fv = None
            little_tip_status_v = None
            little_tip_status_h = None
            ring_tip_status_fh = None
            ring_tip_status_fv = None
            ring_tip_status_v = None
            ring_tip_status_h = None
            thumb_tip_status_fh = None
            thumb_tip_status_fv = None
            thumb_tip_status_v = None
            thumb_tip_status_h = None

            self.output_list = []
            self.common = ''
            ret, img = self.cap.read()
            img = cv2.flip(img, 1)
            h, w, c = img.shape
            landmarks_xyz = self.hands.process(img)
            status = []

            if landmarks_xyz.multi_hand_landmarks:
                for hand_landmark in landmarks_xyz.multi_hand_landmarks:
                    lm_list = []
                    for id, lm in enumerate(hand_landmark.landmark):
                        lm_list.append(lm)
                    finger_fold_status = []
                    for tip in finger_tips:
                        x, y = int(lm_list[tip].x * w), int(lm_list[tip].y * h)

                        # index_tip
                        if lm_list[index_tip - 2].y < lm_list[index_tip - 1].y < lm_list[index_tip].y:
                            index_tip_status_v = "down"
                        if lm_list[index_tip].y < lm_list[index_tip - 1].y < lm_list[index_tip - 2].y:
                            index_tip_status_v = "up"
                        if lm_list[index_tip].x < lm_list[index_tip - 1].x < lm_list[index_tip - 2].x:
                            index_tip_status_h = "left"
                        if lm_list[index_tip - 2].x < lm_list[index_tip - 1].x < lm_list[index_tip].x:
                            index_tip_status_h = "right"
                        if lm_list[index_tip].y < lm_list[index_tip - 2].y:
                            index_tip_status_fv = "fold up"
                        if lm_list[index_tip - 2].y < lm_list[index_tip].y:
                            index_tip_status_fv = "fold down"
                        if lm_list[index_tip].x < lm_list[index_tip - 2].x:
                            index_tip_status_fh = "fold right"
                        if lm_list[index_tip - 2].x < lm_list[index_tip].x:
                            index_tip_status_fh = "fold left"

                        # middle_tip
                        if lm_list[middle_tip - 2].y < lm_list[middle_tip - 1].y < lm_list[middle_tip].y:
                            middle_tip_status_v = "down"
                        if lm_list[middle_tip].y < lm_list[middle_tip - 1].y < lm_list[middle_tip - 2].y:
                            middle_tip_status_v = "up"
                        if lm_list[middle_tip].x < lm_list[middle_tip - 1].x < lm_list[middle_tip - 2].x:
                            middle_tip_status_h = "left"
                        if lm_list[middle_tip - 2].x < lm_list[middle_tip - 1].x < lm_list[middle_tip].x:
                            middle_tip_status_h = "right"
                        if lm_list[middle_tip].y < lm_list[middle_tip - 2].y:
                            middle_tip_status_fv = "fold up"

                        if lm_list[middle_tip - 2].y < lm_list[middle_tip].y:
                            middle_tip_status_fv = "fold down"
                        if lm_list[middle_tip].x < lm_list[middle_tip - 2].x:
                            middle_tip_status_fh = "fold right"
                        if lm_list[middle_tip - 2].x < lm_list[middle_tip].x:
                            middle_tip_status_fh = "fold left"

                        # ring_tip
                        if lm_list[ring_tip - 2].y < lm_list[ring_tip - 1].y < lm_list[ring_tip].y:
                            ring_tip_status_v = "down"
                        if lm_list[ring_tip].y < lm_list[ring_tip - 1].y < lm_list[ring_tip - 2].y:
                            ring_tip_status_v = "up"
                        if lm_list[ring_tip].x < lm_list[ring_tip - 1].x < lm_list[ring_tip - 2].x:
                            ring_tip_status_h = "left"
                        if lm_list[ring_tip - 2].x < lm_list[ring_tip - 1].x < lm_list[ring_tip].x:
                            ring_tip_status_h = "right"
                        if lm_list[ring_tip].y < lm_list[ring_tip - 2].y:
                            ring_tip_status_fv = "fold up"
                        if lm_list[ring_tip - 2].y < lm_list[ring_tip].y:
                            ring_tip_status_fv = "fold down"
                        if lm_list[ring_tip].x < lm_list[ring_tip - 2].x:
                            ring_tip_status_fh = "fold right"
                        if lm_list[ring_tip - 2].x < lm_list[ring_tip].x:
                            ring_tip_status_fh = "fold left"

                        # little_tip
                        if lm_list[little_tip - 2].y < lm_list[little_tip - 1].y < lm_list[little_tip].y:
                            little_tip_status_v = "down"
                        if lm_list[little_tip].y < lm_list[little_tip - 1].y < lm_list[little_tip - 2].y:
                            little_tip_status_v = "up"
                        if lm_list[little_tip].x < lm_list[little_tip - 1].x < lm_list[little_tip - 2].x:
                            little_tip_status_h = "left"
                        if lm_list[little_tip - 2].x < lm_list[little_tip - 1].x < lm_list[little_tip].x:
                            little_tip_status_h = "right"
                        if lm_list[little_tip].y < lm_list[little_tip - 2].y:
                            little_tip_status_fv = "fold up"
                        if lm_list[little_tip - 2].y < lm_list[little_tip].y:
                            little_tip_status_fv = "fold down"
                        if lm_list[little_tip].x < lm_list[little_tip - 2].x:
                            little_tip_status_fh = "fold right"
                        if lm_list[little_tip - 2].x < lm_list[little_tip].x:
                            little_tip_status_fh = "fold left"

                        # thump_tip
                        if lm_list[thumb_tip - 2].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip].y:
                            thumb_tip_status_v = "down"
                        if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y:
                            thumb_tip_status_v = "up"
                        if lm_list[thumb_tip].x < lm_list[thumb_tip - 1].x < lm_list[thumb_tip - 2].x:
                            thumb_tip_status_h = "left"
                        if lm_list[thumb_tip - 2].x < lm_list[thumb_tip - 1].x < lm_list[thumb_tip].x:
                            thumb_tip_status_h = "right"
                        if lm_list[thumb_tip].y < lm_list[thumb_tip - 2].y:
                            thumb_tip_status_fv = "fold up"
                        if lm_list[thumb_tip - 2].y < lm_list[thumb_tip].y:
                            thumb_tip_status_fv = "fold down"
                        if lm_list[thumb_tip].x < lm_list[thumb_tip - 2].x:
                            thumb_tip_status_fh = "fold right"
                        if lm_list[thumb_tip - 2].x < lm_list[thumb_tip].x:
                            thumb_tip_status_fh = "fold left"
                        if lm_list[tip].x < lm_list[tip - 2].x:
                            # cv2.circle(img, (x, y), 15, (0, 255, 0), cv2.FILLED)
                            finger_fold_status.append(True)
                        else:
                            finger_fold_status.append(False)

                    # print(finger_fold_status)

                    x, y = int(lm_list[8].x * w), int(lm_list[8].y * h)
                    # print(x, y)

                    self.mp_draw.draw_landmarks(img, hand_landmark,
                                                self.mp_hands.HAND_CONNECTIONS,
                                                self.mp_draw.DrawingSpec((0, 0, 255), 6, 3),
                                                self.mp_draw.DrawingSpec((0, 255, 0), 4, 2)
                                                )

                    # stop
                    if self.quit == 27:
                        break
                    if lm_list[4].y < lm_list[2].y and lm_list[8].y < lm_list[6].y and lm_list[12].y < lm_list[10].y and \
                            lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y and lm_list[17].x < lm_list[0].x < \
                            lm_list[5].x:
                        cv2.putText(img, "HELLO", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append('HELLO')
                        self.letter="HELLO"
                        continue
                    # Forward
                    if lm_list[3].x > lm_list[4].x and lm_list[8].y < lm_list[6].y and lm_list[12].y > lm_list[10].y and \
                            lm_list[16].y > lm_list[14].y and lm_list[20].y > lm_list[18].y:
                        cv2.putText(img, "Forward", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Forward")
                        self.letter="Forward"
                        continue
                    # Backward
                    if lm_list[3].x > lm_list[4].x and lm_list[3].y < lm_list[4].y and lm_list[8].y > lm_list[6].y and lm_list[
                        12].y < lm_list[10].y and \
                            lm_list[16].y < lm_list[14].y and lm_list[20].y < lm_list[18].y:
                        cv2.putText(img, "Backward", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Backward")
                        self.letter="Backward"
                        continue
                    # Left
                    if lm_list[4].y < lm_list[2].y and lm_list[8].x < lm_list[6].x and lm_list[12].x > lm_list[10].x and \
                            lm_list[16].x > lm_list[14].x and lm_list[20].x > lm_list[18].x and lm_list[5].x < lm_list[0].x:
                        cv2.putText(img, "Left", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Left")
                        self.letter="Left"
                        continue
                    # Right
                    if lm_list[4].y < lm_list[2].y and lm_list[8].x > lm_list[6].x and lm_list[12].x < lm_list[10].x and \
                            lm_list[16].x < lm_list[14].x and lm_list[20].x < lm_list[18].x:
                        cv2.putText(img, "Right", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Right")
                        self.letter="Right"
                        continue
                    if all(finger_fold_status):
                        # like
                        if lm_list[thumb_tip].y < lm_list[thumb_tip - 1].y < lm_list[thumb_tip - 2].y and lm_list[0].x < \
                                lm_list[3].y:
                            self.output_list.append("Like")
                            cv2.putText(img, "Like", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
                            self.letter="Like"
                            continue
                        # Dislike
                        if lm_list[thumb_tip].y > lm_list[thumb_tip - 1].y > lm_list[thumb_tip - 2].y and lm_list[0].x < \
                                lm_list[3].y:
                            cv2.putText(img, "Dislike", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                            self.output_list.append("Dislike")
                            self.letter="Dislike"
                            continue
                    if middle_tip_status_fv == "fold down" and ring_tip_status_fv == "fold down" and thumb_tip_status_v == "up" and index_tip_status_v == "up" and little_tip_status_v == "up":
                        cv2.putText(img, "I Love You", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("I Love You")
                        self.Letter="I LOVE YOU"

                        continue
                    if thumb_tip_status_v == "up" and index_tip_status_fv == "fold down" and ring_tip_status_fv == "fold down" and middle_tip_status_fv == "fold down" and little_tip_status_fv == "fold down":
                        cv2.putText(img, "Yes", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Yes")
                        self.letter="YES"

                        continue
                    if thumb_tip_status_h == "right" and index_tip_status_h == "right" and middle_tip_status_h == "right" and ring_tip_status_h == "right" and little_tip_status_h == "right":
                        cv2.putText(img, "No", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("No")
                        self.letter="NO"

                        continue
                    if thumb_tip_status_v == "up" and index_tip_status_v == "up" and middle_tip_status_v == "up" and little_tip_status_fv == "fold down" and ring_tip_status_fv == "fold down":
                        cv2.putText(img, "Victory", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Victory")
                        self.letter="VICTORY"

                        continue
                    if thumb_tip_status_v == "up" and index_tip_status_fh == "fold left" and middle_tip_status_v == "up" and ring_tip_status_v == "up" and little_tip_status_v == "up":
                        cv2.putText(img, "Nice", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Nice")
                        self.letter="NICE"

                        continue
                    if middle_tip_status_fh == 'fold right' and ring_tip_status_fh == 'fold right' and little_tip_status_fh == 'fold right' and index_tip_status_h == "right" and thumb_tip_status_h == "right":
                        cv2.putText(img, "Green", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("Green")
                        self.letter="GREEN"

                        continue
                    if ring_tip_status_fh == 'fold right' and little_tip_status_fh == 'fold right' and index_tip_status_h == "right" and middle_tip_status_h == "right" and thumb_tip_status_fh == "fold left":
                        cv2.putText(img, "Purple", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("PURPLE")
                        self.letter="PURPLE"

                        continue
                    if middle_tip_status_fh == 'fold right' and ring_tip_status_fh == 'fold right' and index_tip_status_fh == "fold right" and little_tip_status_h == 'right' and thumb_tip_status_v == 'up':
                        cv2.putText(img, "Yellow", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.output_list.append("YELLOW")
                        self.letter="YELLOW"

                        continue
                    if thumb_tip_status_h=="right" and index_tip_status_v=="up" and middle_tip_status_fv=="fold down" and ring_tip_status_fv=="fold down" and little_tip_status_fv=="fold down":
                        cv2.putText(img, "leave", (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
                        self.letter="LEAVE"


            cv2.imshow("Hand Sign Detection", img)
            # cv2.waitKey(10)
            self.quit = cv2.waitKey(1)

            # most common
            self.most_frequent()

            # add to leaned
            self.add_to_learned()

            #text
            self.text_output()
            print(self.letter)

            # Exits the camers when (L) sign is done by the user
            if self.letter == "LEAVE":
                cv2.destroyAllWindows()
                break

    def quitter(self):
        """
        A method that is used to quit the camera when esc key is pressed by the user
            Arguments: None
            Returns: Quits the camera
        (for the TK)
        """
        self.quit = 27

    def most_frequent(self):
        counter = 0
        if len(self.output_list) == 0:
            return
        self.common = self.output_list[0]
        for i in self.output_list:
            curr_frequency = self.output_list.count(i)
            if curr_frequency > counter:
                counter = curr_frequency
                self.common = i

    def text_output(self):
        if self.common == '':
            return
        print(self.common)
        if self.words[self.common] == True:
            print('You learned it \n')
        if self.words[self.common] == False:
            print('This word is new to you \n')

    def voice_output(self, word):
        """
        A method that is used to translate the text to voicerecord
            Arguments: word
            Returns: Displays or Plays the voicerecord
        """
        engine = pyttsx3.init()
        engine.say(word)
        engine.runAndWait()

    def add_to_learned(self):
        if self.common == '':
            return
        self.words[self.common] = True

if __name__=='__main__':
    SignDetection().hand_detection()