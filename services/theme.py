import gradio as gr

theme = gr.themes.Soft(
    primary_hue="neutral",
    secondary_hue="gray",
    text_size="sm",
    spacing_size="sm",
    radius_size="sm",
    font=[gr.themes.GoogleFont('Source Sans Pro'), 'ui-sans-serif', 'system-ui', 'sans-serif'],
).set(
    background_fill_primary='white',
    shadow_drop='rgba(0,0,0,0.05) 0px 1px 2px 0px',
    shadow_drop_lg='0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)',
    shadow_spread='3px',
    block_background_fill='*background_fill_primary',
    block_border_width='1px',
    block_border_width_dark='1px',
    block_label_background_fill='*background_fill_primary',
    block_label_background_fill_dark='*background_fill_secondary',
    block_label_text_color='*neutral_500',
    block_label_text_color_dark='*neutral_200',
    block_label_margin='0',
    block_label_padding='*spacing_sm *spacing_lg',
    block_label_radius='calc(*radius_lg - 1px) 0 calc(*radius_lg - 1px) 0',
    block_label_text_size='*text_sm',
    block_label_text_weight='400',
    block_title_background_fill='none',
    block_title_background_fill_dark='none',
    block_title_text_color='*neutral_500',
    block_title_text_color_dark='*neutral_200',
    block_title_padding='0',
    block_title_radius='none',
    block_title_text_weight='400',
    panel_border_width='0',
    panel_border_width_dark='0',
    checkbox_background_color_selected='*secondary_600',
    checkbox_background_color_selected_dark='*secondary_600',
    checkbox_border_color='*neutral_300',
    checkbox_border_color_dark='*neutral_700',
    checkbox_border_color_focus='*secondary_500',
    checkbox_border_color_focus_dark='*secondary_500',
    checkbox_border_color_selected='*secondary_600',
    checkbox_border_color_selected_dark='*secondary_600',
    checkbox_border_width='*input_border_width',
    checkbox_shadow='*input_shadow',
    checkbox_label_background_fill_selected='*checkbox_label_background_fill',
    checkbox_label_background_fill_selected_dark='*checkbox_label_background_fill',
    checkbox_label_shadow='none',
    checkbox_label_text_color_selected='*checkbox_label_text_color',
    input_background_fill='*neutral_100',
    input_border_color='*border_color_primary',
    input_shadow='none',
    input_shadow_dark='none',
    input_shadow_focus='*input_shadow',
    input_shadow_focus_dark='*input_shadow',
    slider_color='#2563eb',
    slider_color_dark='#2563eb',
    button_shadow='none',
    button_shadow_active='none',
    button_shadow_hover='none',
    button_primary_background_fill='*primary_200',
    button_primary_background_fill_hover='*button_primary_background_fill',
    button_primary_background_fill_hover_dark='*button_primary_background_fill',
    button_primary_text_color='*primary_600',
    button_secondary_background_fill='*neutral_200',
    button_secondary_background_fill_hover='*button_secondary_background_fill',
    button_secondary_background_fill_hover_dark='*button_secondary_background_fill',
    button_secondary_text_color='*neutral_700',
    button_cancel_background_fill_hover='*button_cancel_background_fill',
    button_cancel_background_fill_hover_dark='*button_cancel_background_fill'
)
