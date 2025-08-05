"""
Visualization components for the Technical ATS Resume Expert application.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import streamlit as st
import logging
from typing import Optional
from src.config import Config

logger = logging.getLogger(__name__)

class ChartGenerator:
    """Generates charts and visualizations for the application."""
    
    @staticmethod
    def create_match_pie_chart(match_percentage: int) -> Optional[plt.Figure]:
        """
        Create a pie chart showing match percentage.
        
        Args:
            match_percentage: Match percentage (0-100)
            
        Returns:
            Optional[plt.Figure]: Matplotlib figure or None if error
        """
        try:
            # Validate input
            if not 0 <= match_percentage <= 100:
                logger.warning(f"Invalid match percentage: {match_percentage}")
                match_percentage = max(0, min(100, match_percentage))
            
            # Create figure with better styling
            fig, ax = plt.subplots(figsize=(8, 8), facecolor='white')
            
            # Data for pie chart
            labels = ['Match', 'Gap']
            sizes = [match_percentage, 100 - match_percentage]
            colors = Config.CHART_COLORS
            explode = Config.EXPLODE_VALUES
            
            # Create pie chart with enhanced styling
            wedges, texts, autotexts = ax.pie(
                sizes, 
                explode=explode, 
                labels=labels, 
                colors=colors, 
                autopct='%1.1f%%',
                shadow=True, 
                startangle=90,
                textprops={'fontsize': 12, 'fontweight': 'bold'}
            )
            
            # Enhance text styling
            for autotext in autotexts:
                autotext.set_color('white')
                autotext.set_fontsize(14)
                autotext.set_fontweight('bold')
            
            for text in texts:
                text.set_fontsize(12)
                text.set_fontweight('bold')
            
            # Add title
            ax.set_title(
                f'Resume Match Analysis\n{match_percentage}% Match',
                fontsize=16,
                fontweight='bold',
                pad=20
            )
            
            # Ensure equal aspect ratio
            ax.axis('equal')
            
            # Improve layout
            plt.tight_layout()
            
            logger.info(f"Successfully created pie chart for {match_percentage}% match")
            return fig
            
        except Exception as e:
            logger.error(f"Error creating pie chart: {str(e)}")
            st.error(f"⚠️ Error creating visualization: {str(e)}")
            return None
    
    @staticmethod
    def create_skills_gap_chart(missing_skills: list, present_skills: list) -> Optional[plt.Figure]:
        """
        Create a bar chart showing skills gap analysis.
        
        Args:
            missing_skills: List of missing skills
            present_skills: List of present skills
            
        Returns:
            Optional[plt.Figure]: Matplotlib figure or None if error
        """
        try:
            if not missing_skills and not present_skills:
                return None
                
            fig, ax = plt.subplots(figsize=(10, 6), facecolor='white')
            
            # Prepare data
            categories = ['Present Skills', 'Missing Skills']
            counts = [len(present_skills), len(missing_skills)]
            colors = ['#4CAF50', '#FF5733']
            
            # Create bar chart
            bars = ax.bar(categories, counts, color=colors, alpha=0.8, edgecolor='black', linewidth=1)
            
            # Add value labels on bars
            for bar, count in zip(bars, counts):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                       f'{count}', ha='center', va='bottom', fontweight='bold')
            
            # Styling
            ax.set_title('Skills Gap Analysis', fontsize=16, fontweight='bold', pad=20)
            ax.set_ylabel('Number of Skills', fontsize=12, fontweight='bold')
            ax.grid(axis='y', alpha=0.3)
            
            # Remove top and right spines
            ax.spines['top'].set_visible(False)
            ax.spines['right'].set_visible(False)
            
            plt.tight_layout()
            
            logger.info("Successfully created skills gap chart")
            return fig
            
        except Exception as e:
            logger.error(f"Error creating skills gap chart: {str(e)}")
            return None

class UIComponents:
    """Reusable UI components for the application."""
    
    @staticmethod
    def display_success_message(message: str):
        """Display a success message with styling."""
        st.success(f"✅ {message}")
    
    @staticmethod
    def display_warning_message(message: str):
        """Display a warning message with styling."""
        st.warning(f"⚠️ {message}")
    
    @staticmethod
    def display_error_message(message: str):
        """Display an error message with styling."""
        st.error(f"❌ {message}")
    
    @staticmethod
    def display_info_message(message: str):
        """Display an info message with styling."""
        st.info(f"ℹ️ {message}")
    
    @staticmethod
    def create_download_button(content: str, filename: str, label: str):
        """Create a download button for content."""
        return st.download_button(
            label=label,
            data=content,
            file_name=filename,
            mime='text/plain'
        )
    
    @staticmethod
    def display_metrics(col1, col2, col3, match_percentage: int, total_skills: int, missing_skills: int):
        """Display key metrics in columns."""
        with col1:
            st.metric(
                label="📊 Match Percentage",
                value=f"{match_percentage}%",
                delta=f"{match_percentage - 50}%" if match_percentage != 50 else None
            )
        
        with col2:
            st.metric(
                label="🎯 Total Skills",
                value=total_skills,
                delta=None
            )
        
        with col3:
            st.metric(
                label="❌ Missing Skills",
                value=missing_skills,
                delta=f"-{missing_skills}" if missing_skills > 0 else "0",
                delta_color="inverse"
            )
