# Thinter 라이브러리 사용
import tkinter as tk

# puzzlegame 클래스 사용
class PuzzleGame:
    def __init__(self, root):
        
        # 메인창 제목 설정
        self.root = root
        self.root.title("20가지 수수께끼 맞추기")
        
        #게임 상태 초기화함
        self.score = 0 # 현재 점수
        self.current_question = 0 # 현재 문제 번호

        self.question_label = tk.Label(root, text="") # 문제 표시
        self.question_label.pack(pady=10) # 위젯을 GUI에 추가하고 여백을 설정함

        self.answer_entry = tk.Entry(root) # 답 입력
        self.answer_entry.pack(pady=10) # 위젯을 GUI에 추가하고 여백을 설정함

        self.submit_button = tk.Button(root, text="제출", command=self.check_answer) # 답 제출 버튼 생성
        self.submit_button.pack(pady=10)# 위젯을 GUI에 추가하고 여백을 설정함

        self.result_label = tk.Label(root, text="") # 정답 여부를 표시
        self.result_label.pack(pady=10)# 위젯을 GUI에 추가하고 여백을 설정함

        # 퍼즐 문제, 정답 리스트
        self.puzzle = [
            ["백가지 과일이 죽기 직전을 다른 말로?", "백과사전"],
            ["청바지를 돋보이게 하는 걸음걸이는?", "진주목걸이"],
            ["못 사온다고 해놓고 사온 것은?", "못"],
            ["무가 자기소개를 할 때 하는 말은?", "나무"],
            ["고기 먹을 때 따라오는 개는?", "이쑤시개"],
            ["[힘센 말과 고양이]를 네 글자로?", "슈퍼마켓"],
            ["문제독수리가 불에 타면 어떤 소리가 날까?", "이글이글"],
            ["대학생들의 전투력이 높을 때는?", "개강할때"],
            ["왕과 처음 만날 때 하는 인사는?", "하이킹"],
            ["직접 만든 총은?", "손수건"],
            ["돌하르방이 서커스단을 보고하는 말은?", "제주도좋다"],
            ["결정 장애가 많은 대학은?", "고려대학교"],
            ["사자를 넣고 끓인 국은?", "동물의 왕국"],
            ["돈낭비를 많이 하는 동물은?", "사자"],
            ["중국인이 요리하다 칼에 베이면?", "베이징"],
            ["형을 너무 좋아하는 동생은?", "형광펜"],
            ["중학생과 고등학생만 탈 수 있는 차는?", "중고차"],
            ["이상한 사람들이 모이는 곳은?", "치과"],
            ["달에 사는 물고기는?", "문어"],
            ["검이 정색하면?", "검정색"]
        ]
        #초기화할 때 첫번째 문제 시작
        self.load_question()

    def load_question(self):
        if self.current_question < len(self.puzzle):
            question, answer = self.puzzle[self.current_question]
            self.question_label.config(text=question)
            self.answer_entry.delete(0, tk.END)
            self.result_label.config(text="")
        else:
            # 문제 다풀면 결과 표시
            self.show_result()
    # 답 확인 및 결과 표시
    def check_answer(self):
        #내가 쓴 답이랑 정답 표시
        user_input = self.answer_entry.get()
        correct_answer = self.puzzle[self.current_question][1]
        #정답이면 점수 +1, 틀리면 틀린 결과 표시
        if user_input == correct_answer:
            self.score += 1
            self.result_label.config(text=f"정답입니다! 현재 점수는 {self.score}점 입니다.")
        else:
            self.result_label.config(text=f"틀렸습니다. 정답은 {correct_answer}입니다.")
        # 다음 문제 
        self.current_question += 1
        self.load_question()
    # 최종 결과 표시
    def show_result(self):
        # 총 문제 개수, 맞힌 문제 수 표시 및 각 문제의 답을 정렬
        result_text = f"총 {len(self.puzzle)}문제 중 {self.score}문제를 맞혔습니다.\n\n정답 목록:\n"
        result_text += "\n".join([f"{i + 1}. {question} - {answer}" for i, (question, answer) in enumerate(self.puzzle)])
        self.question_label.config(text=result_text)
        self.answer_entry.destroy()
        self.submit_button.destroy()
# 메인 코드 
if __name__ == "__main__":
    # Tkinter의 메인 창 생성, puzzlegame 클래스 생성
    root = tk.Tk()
    app = PuzzleGame(root)
    # Tkinter 실행 하여 GUI 표시
    root.mainloop()