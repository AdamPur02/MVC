using System.ComponentModel.DataAnnotations;

namespace ExpenseTracker.Models
{
    public class Expense
    {
        public int Id { get; set; }

        [Required(ErrorMessage = "Category is required.")]
        [StringLength(50, ErrorMessage = "Category cannot exceed 50 characters.")]
        [Display(Name = "Category")]
        public string Category { get; set; } = string.Empty;

        [Required(ErrorMessage = "Amount is required.")]
        [Range(0.01, 1000000, ErrorMessage = "Amount must be greater than 0.")]
        [Display(Name = "Amount")]
        public decimal Amount { get; set; }

        [Required(ErrorMessage = "Date is required.")]
        [DataType(DataType.Date)]
        [Display(Name = "Date")]
        public DateTime Date { get; set; }
    }
}