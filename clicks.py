import time
import pyautogui

class Clicker:
    def realizar_clic(self):
        # Lógica para realizar clic en la pantalla usando pyautogui
        pyautogui.click()

    def time_measure(self):
      timeStart=time.time()
      final=0
      duration=0
      try:
          while True:
              self.realizar_clic()
              time.sleep(20)
      except KeyboardInterrupt:
          timeEnd=time.time()
          duration=timeEnd-timeStart
          final=duration/60
      print(f"La ejecucion se detuvo. Tiempo total {final} minutos")
      return duration


if __name__ == '__main__':
    # Instancia la clase Clicker
    clicker = Clicker()

    # Llama al método para realizar clic
    clicker.time_measure()
