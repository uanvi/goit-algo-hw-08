import heapq

def minimum_cost_to_merge_cables(cables):
    # Ініціалізуємо купу, найменші будуть зверху
    heapq.heapify(cables)
    total_cost = 0
    
    while len(cables) > 1:
        # Вибираємо два найменші кабелі
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        
        # Зливаємо
        merge_cost = first + second
        total_cost += merge_cost
        
        # Додаємо новий кабель до купи
        heapq.heappush(cables, merge_cost)
    
    return total_cost

cables = [5, 2, 3, 9]
minimum_cost = minimum_cost_to_merge_cables(cables)
print("Мінімальні витрати:", minimum_cost)
